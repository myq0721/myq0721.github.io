#!/usr/bin/env python3
"""30-year portfolio backtest (CNY, annual rebalancing)."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from portfolio_data import (
    END,
    START,
    backtest_portfolio,
    compute_metrics,
    load_asset_returns,
)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "source" / "images" / "portfolio-research"
METRICS_PATH = OUTPUT_DIR / "metrics.json"

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

PORTFOLIOS = {
    "组合1_全球分散": {
        "nasdaq": 0.30,
        "sp500": 0.20,
        "euro": 0.10,
        "nikkei": 0.10,
        "gold": 0.10,
        "cash": 0.20,
    },
    "组合2_沪深300偏重": {
        "nasdaq": 0.30,
        "sp500": 0.20,
        "csi300": 0.20,
        "gold": 0.10,
        "cash": 0.20,
    },
    "组合3_黄金偏重": {
        "nasdaq": 0.30,
        "sp500": 0.20,
        "csi300": 0.10,
        "gold": 0.20,
        "cash": 0.20,
    },
    "组合4_四等分均衡": {
        "sp500": 0.25,
        "gold": 0.25,
        "bonds": 0.25,
        "cash": 0.25,
    },
}

COLORS = {
    "组合1_全球分散": "#2563eb",
    "组合2_沪深300偏重": "#dc2626",
    "组合3_黄金偏重": "#d97706",
    "组合4_四等分均衡": "#059669",
}


def plot_cumulative(nav_df: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in nav_df.columns:
        ax.plot(nav_df.index, nav_df[col], label=col, color=COLORS.get(col), linewidth=2)
    ax.set_title("四种组合累计净值对比（人民币，起点=1）", fontsize=14)
    ax.set_xlabel("日期")
    ax.set_ylabel("净值")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_drawdown(nav_df: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in nav_df.columns:
        nav = nav_df[col]
        ax.plot(nav.index, (nav / nav.cummax() - 1) * 100, label=col, color=COLORS.get(col), linewidth=1.5)
    ax.set_title("四种组合历史回撤", fontsize=14)
    ax.set_xlabel("日期")
    ax.set_ylabel("回撤 (%)")
    ax.legend(loc="lower left")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_risk_return(metrics: dict, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    for name, m in metrics.items():
        x = abs(m["max_drawdown_pct"])
        y = m["annualized_return_pct"]
        ax.scatter(x, y, s=120, color=COLORS.get(name, "#333"), zorder=3)
        ax.annotate(
            f"{name}\n夏普 {m['sharpe_ratio']:.2f}",
            (x, y),
            textcoords="offset points",
            xytext=(8, 8),
            fontsize=9,
        )
    ax.set_title("风险–收益散点图（横轴：最大回撤绝对值）", fontsize=14)
    ax.set_xlabel("最大回撤 (%)")
    ax.set_ylabel("年化收益率 (%)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_annual_returns(annual_df: pd.DataFrame, out: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)
    for ax, col in zip(axes.flatten(), annual_df.columns):
        colors = ["#dc2626" if v < 0 else "#2563eb" for v in annual_df[col]]
        ax.bar(annual_df.index.year.astype(str), annual_df[col] * 100, color=colors, width=0.8)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(col, fontsize=11)
        ax.set_ylabel("年收益率 (%)")
        ax.tick_params(axis="x", rotation=45, labelsize=7)
        ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("四种组合年度收益率", fontsize=14, y=1.01)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Fetching data...")
    asset_returns = load_asset_returns()
    print(
        f"Sample: {asset_returns.index[0].date()} -> {asset_returns.index[-1].date()}, "
        f"{len(asset_returns)} months"
    )

    rf = asset_returns["cash"]
    port_returns: dict[str, pd.Series] = {}
    metrics: dict[str, dict] = {}
    for name, weights in PORTFOLIOS.items():
        port_returns[name] = backtest_portfolio(asset_returns, weights)
        metrics[name] = compute_metrics(port_returns[name], rf)

    nav_df = pd.DataFrame({n: (1 + r).cumprod() for n, r in port_returns.items()})
    annual_df = pd.DataFrame({n: (1 + r).resample("YE").prod() - 1 for n, r in port_returns.items()})

    plot_cumulative(nav_df, OUTPUT_DIR / "cumulative_nav.png")
    plot_drawdown(nav_df, OUTPUT_DIR / "drawdown.png")
    plot_risk_return(metrics, OUTPUT_DIR / "risk_return.png")
    plot_annual_returns(annual_df, OUTPUT_DIR / "annual_returns.png")

    payload = {
        "methodology": {
            "start": START,
            "end": END,
            "currency": "CNY",
            "rebalancing": "annual (December month-end)",
        },
        "portfolios": PORTFOLIOS,
        "metrics": metrics,
        "sample_period": {
            "start": str(asset_returns.index[0].date()),
            "end": str(asset_returns.index[-1].date()),
            "months": len(asset_returns),
        },
    }
    METRICS_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n=== Metrics ===")
    for name, m in metrics.items():
        print(
            f"{name}: ann={m['annualized_return_pct']}% "
            f"maxDD={m['max_drawdown_pct']}% sharpe={m['sharpe_ratio']}"
        )
    print(f"\nOutputs -> {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
