#!/usr/bin/env python3
"""DD30 portfolio analysis: dual-window metrics, grid search, Monte Carlo."""

from __future__ import annotations

import json
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from portfolio_data import (
    ASSET_NAMES,
    RECENT_START,
    backtest_portfolio,
    dual_window_metrics,
    load_core_six_assets,
)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "source" / "images" / "portfolio-dd30"
METRICS_PATH = OUTPUT_DIR / "metrics.json"

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

CANDIDATES = {
    "Blog_博客方案": {
        "nasdaq": 0.40,
        "gold": 0.20,
        "csi300": 0.10,
        "cash": 0.30,
    },
    "R3_回测组合3": {
        "nasdaq": 0.30,
        "sp500": 0.20,
        "csi300": 0.10,
        "gold": 0.20,
        "cash": 0.20,
    },
    "6040_经典股债": {
        "nasdaq": 0.30,
        "sp500": 0.30,
        "bonds": 0.40,
    },
    "PP_永久组合": {
        "sp500": 0.25,
        "gold": 0.25,
        "bonds": 0.25,
        "cash": 0.25,
    },
    "AW_全天候简化": {
        "nasdaq": 0.15,
        "sp500": 0.15,
        "bonds": 0.55,
        "gold": 0.15,
    },
}

COLORS = {
    "Blog_博客方案": "#2563eb",
    "R3_回测组合3": "#d97706",
    "6040_经典股债": "#7c3aed",
    "PP_永久组合": "#059669",
    "AW_全天候简化": "#0891b2",
    "DD30_推荐方案": "#dc2626",
}

DD30_DD_MIN = -40.0
DD30_DD_MAX = -22.0
WEIGHT_STEP = 0.05
MAX_ASSET_WEIGHT = 0.60
SCORE_W10 = 0.65
SCORE_W30 = 0.35


def generate_weight_grid(
    assets: list[str],
    step: float = WEIGHT_STEP,
    max_weight: float = MAX_ASSET_WEIGHT,
) -> list[dict[str, float]]:
    units_total = int(round(1 / step))
    max_units = int(round(max_weight / step))
    n = len(assets)
    results: list[dict[str, float]] = []

    def rec(idx: int, remaining: int, acc: list[int]) -> None:
        if idx == n - 1:
            if 0 <= remaining <= max_units:
                weights = [u * step for u in (*acc, remaining)]
                results.append(dict(zip(assets, weights)))
            return
        for u in range(0, min(remaining, max_units) + 1):
            rec(idx + 1, remaining - u, [*acc, u])

    rec(0, units_total, [])
    return results


def optimize_dd30(returns: pd.DataFrame, rf: pd.Series) -> tuple[dict[str, float], list[dict]]:
    coarse = generate_weight_grid(ASSET_NAMES, step=0.10, max_weight=0.60)
    print(f"Coarse grid: {len(coarse)} combinations...", flush=True)
    feasible = _search_grid(returns, rf, coarse)

    if not feasible:
        raise RuntimeError("No feasible portfolio in drawdown band")

    feasible.sort(key=lambda x: (-x["dual"]["weighted_score"], -x["tie_break"]))
    best_w = feasible[0]["weights"]

    refine_set: set[tuple] = set()
    base = {a: int(round(best_w.get(a, 0) / 0.05)) for a in ASSET_NAMES}
    for deltas in _delta_grid(len(ASSET_NAMES), max_delta=2):
        units = [max(0, min(12, base[a] + deltas[i])) for i, a in enumerate(ASSET_NAMES)]
        if sum(units) != 20:
            continue
        w = {a: units[i] * 0.05 for i, a in enumerate(ASSET_NAMES)}
        refine_set.add(tuple(w[a] for a in ASSET_NAMES))
    refine = [dict(zip(ASSET_NAMES, t)) for t in refine_set]
    print(f"Refine grid: {len(refine)} combinations...", flush=True)
    feasible.extend(_search_grid(returns, rf, refine))

    feasible_list = list({tuple(sorted(x["weights"].items())): x for x in feasible}.values())
    feasible_list.sort(key=lambda x: (-x["dual"]["weighted_score"], -x["tie_break"]))
    return feasible_list[0]["weights"], feasible_list[:20]


def _delta_grid(n: int, max_delta: int) -> list[tuple[int, ...]]:
    from itertools import product

    return list(product(range(-max_delta, max_delta + 1), repeat=n))


def _search_grid(returns: pd.DataFrame, rf: pd.Series, grid: list[dict[str, float]]) -> list[dict]:
    feasible: list[dict] = []
    for i, weights in enumerate(grid):
        port = backtest_portfolio(returns, weights)
        dual = dual_window_metrics(port, rf)
        dd30 = dual["30y"].get("max_drawdown_pct", -100)
        if dd30 < DD30_DD_MIN or dd30 > DD30_DD_MAX:
            continue
        ann10 = dual["10y"].get("annualized_return_pct") or 0
        ann30 = dual["30y"].get("annualized_return_pct") or 0
        feasible.append(
            {
                "weights": weights,
                "dual": dual,
                "tie_break": SCORE_W10 * ann10 + SCORE_W30 * ann30,
            }
        )
        if (i + 1) % 500 == 0:
            print(f"  scanned {i+1}/{len(grid)}, feasible={len(feasible)}", flush=True)
    return feasible


def rolling_10y_annualized(port_ret: pd.Series) -> pd.Series:
    out: list[float] = []
    idx: list[pd.Timestamp] = []
    for i in range(120, len(port_ret) + 1):
        window = port_ret.iloc[i - 120 : i]
        ann = (1 + window).prod() ** (12 / 120) - 1
        out.append(ann)
        idx.append(port_ret.index[i - 1])
    return pd.Series(out, index=idx)


def weighted_block_bootstrap(
    port_ret: pd.Series,
    n_paths: int = 1000,
    horizon: int = 360,
    block: int = 12,
    recent_prob: float = 0.70,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    rng = random.Random(seed)
    cutover = pd.Timestamp(RECENT_START)
    early = port_ret.loc[port_ret.index < cutover]
    recent = port_ret.loc[port_ret.index >= cutover]

    def block_starts(series: pd.Series) -> list[int]:
        return list(range(0, len(series) - block + 1))

    starts_early = block_starts(early)
    starts_recent = block_starts(recent)
    vals_early = early.values
    vals_recent = recent.values

    nav_paths = np.zeros((n_paths, horizon + 1))
    maxdds = np.zeros(n_paths)

    for p in range(n_paths):
        collected: list[float] = []
        while len(collected) < horizon:
            use_recent = rng.random() < recent_prob
            if use_recent and starts_recent:
                s = rng.choice(starts_recent)
                chunk = vals_recent[s : s + block].tolist()
            elif starts_early:
                s = rng.choice(starts_early)
                chunk = vals_early[s : s + block].tolist()
            else:
                s = rng.choice(starts_recent)
                chunk = vals_recent[s : s + block].tolist()
            collected.extend(chunk)
        r = np.array(collected[:horizon])
        nav = np.cumprod(np.concatenate([[1.0], 1 + r]))
        nav_paths[p] = nav
        peak = np.maximum.accumulate(nav)
        maxdds[p] = np.min(nav / peak - 1)

    return nav_paths, maxdds


def plot_cumulative(nav_df: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in nav_df.columns:
        ax.plot(nav_df.index, nav_df[col], label=col, color=COLORS.get(col, "#333"), linewidth=2)
    ax.set_title("候选组合与 DD30 推荐：累计净值（人民币）", fontsize=14)
    ax.set_xlabel("日期")
    ax.set_ylabel("净值")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_drawdown(nav_df: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in nav_df.columns:
        nav = nav_df[col]
        ax.plot(nav.index, (nav / nav.cummax() - 1) * 100, label=col, color=COLORS.get(col, "#333"), linewidth=1.5)
    ax.axhline(-30, color="#9ca3af", linestyle="--", linewidth=1.2, label="−30% 参考线")
    ax.set_title("历史回撤曲线", fontsize=14)
    ax.set_xlabel("日期")
    ax.set_ylabel("回撤 (%)")
    ax.legend(loc="lower left", fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_rolling_10y(rolling: dict[str, pd.Series], out: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for name, series in rolling.items():
        ax.plot(series.index, series * 100, label=name, color=COLORS.get(name, "#333"), linewidth=1.5)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(pd.Timestamp(RECENT_START), color="#9ca3af", linestyle=":", alpha=0.8, label="近十年起点")
    ax.set_title("滚动 10 年年化收益率", fontsize=14)
    ax.set_xlabel("日期")
    ax.set_ylabel("年化收益率 (%)")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_mc_fan(nav_paths: np.ndarray, out: Path) -> None:
    months = nav_paths.shape[1] - 1
    x = np.arange(months + 1)
    p10 = np.percentile(nav_paths, 10, axis=0)
    p50 = np.percentile(nav_paths, 50, axis=0)
    p90 = np.percentile(nav_paths, 90, axis=0)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.fill_between(x, p10, p90, alpha=0.25, color="#2563eb", label="P10–P90")
    ax.plot(x, p50, color="#1d4ed8", linewidth=2, label="中位数 P50")
    ax.set_title("DD30 蒙特卡洛模拟：30 年净值扇形图（加权自助法）", fontsize=14)
    ax.set_xlabel("月份")
    ax.set_ylabel("净值")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_mc_maxdd_hist(maxdds: np.ndarray, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(maxdds * 100, bins=40, color="#2563eb", alpha=0.75, edgecolor="white")
    ax.axvline(-30, color="#dc2626", linestyle="--", linewidth=1.5, label="−30% 参考线")
    ax.axvline(np.median(maxdds) * 100, color="#059669", linestyle="-", linewidth=1.5, label=f"中位数 {np.median(maxdds)*100:.1f}%")
    ax.set_title("蒙特卡洛：模拟路径最大回撤分布（DD30 推荐组合）", fontsize=14)
    ax.set_xlabel("最大回撤 (%)")
    ax.set_ylabel("路径数量")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_correlation(returns: pd.DataFrame, out: Path) -> None:
    corr = returns[ASSET_NAMES].corr()
    labels = ["纳指", "标普", "沪深300", "黄金", "债券", "现金"]
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(labels)), labels, rotation=45, ha="right")
    ax.set_yticks(range(len(labels)), labels)
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=9)
    ax.set_title("六类资产月度收益相关性（1996–2025）", fontsize=14)
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_return_vs_drawdown(candidates_dual: dict, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 6))
    for name, dual in candidates_dual.items():
        m = dual["30y"]
        x = abs(m["max_drawdown_pct"])
        y = m["annualized_return_pct"]
        ax.scatter(x, y, s=100, color=COLORS.get(name, "#333"), zorder=3)
        ax.annotate(name.replace("_", "\n"), (x, y), textcoords="offset points", xytext=(6, 6), fontsize=8)
    ax.axvline(30, color="#9ca3af", linestyle="--", alpha=0.7, label="30% 回撤参考")
    ax.set_title("30 年收益–回撤散点（候选 + DD30）", fontsize=14)
    ax.set_xlabel("最大回撤 (%)")
    ax.set_ylabel("年化收益率 (%)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_metrics_30y_vs_10y(candidates_dual: dict, out: Path) -> None:
    names = list(candidates_dual.keys())
    ann30 = [candidates_dual[n]["30y"]["annualized_return_pct"] for n in names]
    ann10 = [candidates_dual[n]["10y"]["annualized_return_pct"] for n in names]
    dd30 = [abs(candidates_dual[n]["30y"]["max_drawdown_pct"]) for n in names]
    dd10 = [abs(candidates_dual[n]["10y"]["max_drawdown_pct"]) for n in names]

    x = np.arange(len(names))
    w = 0.35
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].bar(x - w / 2, ann30, w, label="30Y 年化%", color="#2563eb")
    axes[0].bar(x + w / 2, ann10, w, label="10Y 年化%", color="#93c5fd")
    axes[0].set_xticks(x, [n.replace("_", "\n") for n in names], fontsize=7)
    axes[0].set_ylabel("年化收益率 (%)")
    axes[0].set_title("年化收益：全周期 vs 近十年")
    axes[0].legend()
    axes[0].grid(True, axis="y", alpha=0.3)

    axes[1].bar(x - w / 2, dd30, w, label="30Y |回撤|%", color="#dc2626")
    axes[1].bar(x + w / 2, dd10, w, label="10Y |回撤|%", color="#fca5a5")
    axes[1].axhline(30, color="#9ca3af", linestyle="--", linewidth=1)
    axes[1].set_xticks(x, [n.replace("_", "\n") for n in names], fontsize=7)
    axes[1].set_ylabel("最大回撤绝对值 (%)")
    axes[1].set_title("最大回撤：全周期 vs 近十年")
    axes[1].legend()
    axes[1].grid(True, axis="y", alpha=0.3)

    fig.suptitle("双窗口指标对比", fontsize=14, y=1.02)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)


def format_weights(weights: dict[str, float]) -> dict[str, float]:
    return {k: round(v, 2) for k, v in weights.items() if v > 0}


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Loading six-asset returns...")
    returns = load_core_six_assets()
    rf = returns["cash"]
    print(f"Sample: {returns.index[0].date()} -> {returns.index[-1].date()}, {len(returns)} months")

    print("Optimizing DD30...")
    dd30_weights, top_feasible = optimize_dd30(returns, rf)
    all_portfolios = {**CANDIDATES, "DD30_推荐方案": dd30_weights}

    port_returns: dict[str, pd.Series] = {}
    dual_metrics: dict[str, dict] = {}
    for name, weights in all_portfolios.items():
        port_returns[name] = backtest_portfolio(returns, weights)
        dual_metrics[name] = dual_window_metrics(port_returns[name], rf)

    nav_df = pd.DataFrame({n: (1 + r).cumprod() for n, r in port_returns.items()})
    rolling = {n: rolling_10y_annualized(r) for n, r in port_returns.items()}

    print("Monte Carlo (DD30)...")
    nav_paths, maxdds = weighted_block_bootstrap(port_returns["DD30_推荐方案"])

    plot_cumulative(nav_df, OUTPUT_DIR / "cumulative_nav.png")
    plot_drawdown(nav_df, OUTPUT_DIR / "drawdown.png")
    plot_rolling_10y(rolling, OUTPUT_DIR / "rolling_10y_return.png")
    plot_mc_fan(nav_paths, OUTPUT_DIR / "monte_carlo_fan.png")
    plot_mc_maxdd_hist(maxdds, OUTPUT_DIR / "monte_carlo_maxdd_hist.png")
    plot_correlation(returns, OUTPUT_DIR / "correlation_matrix.png")
    plot_return_vs_drawdown(dual_metrics, OUTPUT_DIR / "return_vs_drawdown.png")
    plot_metrics_30y_vs_10y(dual_metrics, OUTPUT_DIR / "metrics_30y_vs_10y.png")

    mc_summary = {
        "median_final_nav": round(float(np.median(nav_paths[:, -1])), 3),
        "p10_final_nav": round(float(np.percentile(nav_paths[:, -1], 10)), 3),
        "p90_final_nav": round(float(np.percentile(nav_paths[:, -1], 90)), 3),
        "median_max_drawdown_pct": round(float(np.median(maxdds) * 100), 2),
        "p75_max_drawdown_pct": round(float(np.percentile(maxdds, 25) * 100), 2),
        "paths": len(maxdds),
        "recent_block_weight": 0.70,
    }

    payload = {
        "methodology": {
            "currency": "CNY",
            "rebalancing": "annual",
            "score": f"{SCORE_W10}*Calmar_10Y + {SCORE_W30}*Calmar_30Y",
            "drawdown_band_30y": [DD30_DD_MIN, DD30_DD_MAX],
            "monte_carlo": "block bootstrap 12m, 70% recent / 30% early",
        },
        "dd30_weights": format_weights(dd30_weights),
        "candidates": {k: format_weights(v) for k, v in CANDIDATES.items()},
        "dual_metrics": dual_metrics,
        "monte_carlo_dd30": mc_summary,
        "top_feasible_count": len(top_feasible),
    }
    METRICS_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    d = dual_metrics["DD30_推荐方案"]
    print("\n=== DD30 ===")
    print("Weights:", format_weights(dd30_weights))
    print(f"30Y: ann={d['30y']['annualized_return_pct']}% DD={d['30y']['max_drawdown_pct']}% sharpe={d['30y']['sharpe_ratio']}")
    print(f"10Y: ann={d['10y']['annualized_return_pct']}% DD={d['10y']['max_drawdown_pct']}% sharpe={d['10y']['sharpe_ratio']}")
    print(f"Score={d['weighted_score']}")
    print(f"MC median maxDD={mc_summary['median_max_drawdown_pct']}%")
    print(f"Outputs -> {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
