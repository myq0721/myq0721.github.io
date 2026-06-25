"""Shared portfolio data loading and backtest utilities."""

from __future__ import annotations

import io
import time
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

import akshare as ak
import numpy as np
import pandas as pd

START = "1996-01-01"
END = "2025-12-31"
RECENT_START = "2016-01-01"
CACHE_DIR = Path(__file__).resolve().parent / "data_cache"

ASSET_NAMES = ["nasdaq", "sp500", "csi300", "gold", "bonds", "cash"]


def fetch_url_bytes(url: str, retries: int = 5) -> bytes:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return urlopen(req, timeout=180).read()
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            print(f"  url retry {attempt + 1}/{retries}: {exc}")
            time.sleep(4 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def fetch_fred_series(series_id: str) -> pd.Series:
    cache = CACHE_DIR / f"fred_{series_id}.csv"
    if cache.exists():
        df = pd.read_csv(cache, parse_dates=["date"])
        return df.set_index("date")["value"].dropna()
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    df = pd.read_csv(io.BytesIO(fetch_url_bytes(url)))
    df.columns = ["date", "value"]
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache, index=False)
    return df.set_index("date")["value"].dropna()


def parse_french_monthly_csv(zip_name: str, csv_name: str, header_marker: str) -> pd.DataFrame:
    cache = CACHE_DIR / f"french_{csv_name}"
    if cache.exists():
        return pd.read_csv(cache, parse_dates=["date"], index_col="date")

    url = f"https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/{zip_name}"
    zf = zipfile.ZipFile(io.BytesIO(fetch_url_bytes(url)))
    lines = zf.read(csv_name).decode().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(header_marker))
    header = [h.strip() for h in lines[start].split(",")]
    rows = []
    for line in lines[start + 1 :]:
        if not line or not line[0].isdigit():
            break
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < len(header):
            continue
        yyyymm = parts[0]
        if len(yyyymm) != 6:
            continue
        dt = pd.Timestamp(f"{yyyymm[:4]}-{yyyymm[4:]}-01") + pd.offsets.MonthEnd(0)
        vals = []
        ok = True
        for v in parts[1 : len(header)]:
            fv = float(v)
            if fv <= -90:
                ok = False
                break
            vals.append(fv / 100.0)
        if ok:
            rows.append([dt, *vals])

    df = pd.DataFrame(rows, columns=["date", *header[1:]])
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache)
    return df


def load_french_factors() -> pd.DataFrame:
    df = parse_french_monthly_csv(
        "F-F_Research_Data_Factors_CSV.zip",
        "F-F_Research_Data_Factors.csv",
        ",Mkt-RF",
    )
    df["sp500"] = df["Mkt-RF"] + df["RF"]
    return df


def load_french_hitec() -> pd.Series:
    df = parse_french_monthly_csv(
        "10_Industry_Portfolios_CSV.zip",
        "10_Industry_Portfolios.csv",
        ",NoDur",
    )
    return df["HiTec"]


def parse_french_region(zip_name: str, csv_name: str) -> pd.Series:
    df = parse_french_monthly_csv(zip_name, csv_name, ",Mkt-RF")
    return df["Mkt-RF"] + df["RF"]


def load_akshare_index(symbol: str) -> pd.Series:
    cache = CACHE_DIR / f"ak_{symbol}.csv"
    if cache.exists():
        df = pd.read_csv(cache, parse_dates=["date"], index_col="date")
        return df["close"].astype(float)
    df = ak.stock_zh_index_daily(symbol=symbol)
    df["date"] = pd.to_datetime(df["date"])
    series = df.set_index("date")["close"].astype(float).sort_index()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    series.to_frame("close").to_csv(cache)
    return series


def monthly_returns(prices: pd.Series) -> pd.Series:
    monthly = prices.resample("ME").last().dropna()
    return monthly.pct_change().dropna()


def cny_returns_from_usd(asset_ret: pd.Series, usdcny_ret: pd.Series) -> pd.Series:
    aligned = pd.concat([asset_ret, usdcny_ret], axis=1, join="inner").dropna()
    aligned.columns = ["asset", "fx"]
    return (1 + aligned["asset"]) * (1 + aligned["fx"]) - 1


def cny_returns_from_fx_cross(asset_ret: pd.Series, fx_ret: pd.Series) -> pd.Series:
    aligned = pd.concat([asset_ret, fx_ret], axis=1, join="inner").dropna()
    aligned.columns = ["asset", "fx"]
    return (1 + aligned["asset"]) * (1 + aligned["fx"]) - 1


def fx_monthly_returns_from_fred() -> tuple[pd.Series, pd.Series, pd.Series]:
    cny_per_usd = fetch_fred_series("DEXCHUS")
    usd_per_eur = fetch_fred_series("DEXUSEU")
    jpy_per_usd = fetch_fred_series("DEXJPUS")
    cny_per_eur = cny_per_usd.reindex(usd_per_eur.index, method="ffill") * usd_per_eur
    cny_per_jpy = cny_per_usd.reindex(jpy_per_usd.index, method="ffill") / jpy_per_usd
    usdcny = cny_per_usd.resample("ME").last().pct_change().dropna()
    eurcny = cny_per_eur.resample("ME").last().pct_change().dropna()
    jpycny = cny_per_jpy.resample("ME").last().pct_change().dropna()
    return usdcny, eurcny, jpycny


def europe_cny_returns(europe: pd.Series, usdcny_ret: pd.Series, eurcny_ret: pd.Series) -> pd.Series:
    via_usd = cny_returns_from_usd(europe, usdcny_ret)
    via_eur = cny_returns_from_fx_cross(europe, eurcny_ret)
    cutover = eurcny_ret.index.min()
    head = via_usd[via_usd.index < cutover]
    tail = via_eur[via_eur.index >= cutover]
    combined = pd.concat([head, tail])
    return combined[~combined.index.duplicated(keep="last")].sort_index()


def build_bond_series(ff_rf: pd.Series) -> pd.Series:
    return (ff_rf * 0.6 + 0.0025).dropna()


def build_gold_usd_returns() -> pd.Series:
    cache = CACHE_DIR / "gold_monthly_usd.csv"
    if cache.exists():
        gold = pd.read_csv(cache, parse_dates=["date"], index_col="date")["price"]
    else:
        url = "https://raw.githubusercontent.com/datasets/gold-prices/master/data/monthly.csv"
        df = pd.read_csv(io.BytesIO(fetch_url_bytes(url)))
        df.columns = ["date", "price"]
        df["date"] = pd.to_datetime(df["date"])
        gold = df.set_index("date")["price"].astype(float)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        gold.to_frame("price").to_csv(cache)
    return monthly_returns(gold)


def build_csi300_series() -> pd.Series:
    csi = load_akshare_index("sh000300")
    sse = load_akshare_index("sh000001")
    csi_ret = monthly_returns(csi)
    sse_ret = monthly_returns(sse)
    csi_start = csi_ret.index.min()
    combined = sse_ret[sse_ret.index < csi_start]
    combined = pd.concat([combined, csi_ret])
    return combined[~combined.index.duplicated(keep="last")].sort_index()


def load_asset_returns() -> pd.DataFrame:
    print("Loading FRED FX...")
    usdcny_ret, eurcny_ret, jpycny_ret = fx_monthly_returns_from_fred()

    print("Loading Kenneth French data...")
    ff = load_french_factors()
    hitec = load_french_hitec()
    europe = parse_french_region("Europe_3_Factors_CSV.zip", "Europe_3_Factors.csv")
    japan = parse_french_region("Japan_3_Factors_CSV.zip", "Japan_3_Factors.csv")

    print("Loading akshare China indices...")
    assets = pd.DataFrame()
    assets["nasdaq"] = cny_returns_from_usd(hitec, usdcny_ret)
    assets["sp500"] = cny_returns_from_usd(ff["sp500"], usdcny_ret)
    assets["euro"] = europe_cny_returns(europe, usdcny_ret, eurcny_ret)
    assets["nikkei"] = cny_returns_from_fx_cross(japan, jpycny_ret)
    assets["csi300"] = build_csi300_series()
    assets["gold"] = cny_returns_from_usd(build_gold_usd_returns(), usdcny_ret)
    assets["bonds"] = cny_returns_from_usd(build_bond_series(ff["RF"]), usdcny_ret)
    assets["cash"] = cny_returns_from_usd(ff["RF"], usdcny_ret)

    return assets.loc[START:END].dropna(how="any")


def load_core_six_assets() -> pd.DataFrame:
    """Six-asset universe for DD30 analysis (no euro/nikkei)."""
    full = load_asset_returns()
    return full[ASSET_NAMES].copy()


def backtest_portfolio(returns: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    assets = list(weights.keys())
    w = np.array([weights[a] for a in assets])
    sub = returns[assets].copy()

    port_ret: list[float] = []
    dates = sub.index.tolist()
    holdings = w.copy()

    for i, dt in enumerate(dates):
        r = sub.loc[dt].values
        port_ret.append(float(np.dot(holdings, r)))
        holdings = holdings * (1 + r)
        holdings = holdings / holdings.sum()
        if i < len(dates) - 1 and dt.month == 12:
            holdings = w.copy()

    return pd.Series(port_ret, index=dates, name="portfolio")


def compute_metrics(port_ret: pd.Series, rf_ret: pd.Series | None = None) -> dict:
    if len(port_ret) < 12:
        return {}
    if rf_ret is None:
        rf_ret = port_ret * 0.0
    rf_aligned = rf_ret.reindex(port_ret.index).fillna(0)

    nav = (1 + port_ret).cumprod()
    years = max((port_ret.index[-1] - port_ret.index[0]).days / 365.25, 1 / 12)
    ann_return = nav.iloc[-1] ** (1 / years) - 1
    ann_vol = port_ret.std() * np.sqrt(12)
    rf_ann = (1 + rf_aligned).prod() ** (1 / years) - 1
    sharpe = (ann_return - rf_ann) / ann_vol if ann_vol > 0 else np.nan
    max_dd = (nav / nav.cummax() - 1).min()
    calmar = ann_return / abs(max_dd) if max_dd < 0 else np.nan

    return {
        "start": str(port_ret.index[0].date()),
        "end": str(port_ret.index[-1].date()),
        "years": round(years, 2),
        "total_return_pct": round((nav.iloc[-1] - 1) * 100, 2),
        "annualized_return_pct": round(ann_return * 100, 2),
        "annualized_volatility_pct": round(ann_vol * 100, 2),
        "max_drawdown_pct": round(max_dd * 100, 2),
        "sharpe_ratio": round(sharpe, 3),
        "calmar_ratio": round(calmar, 3),
        "risk_free_annualized_pct": round(rf_ann * 100, 2),
        "final_nav": round(nav.iloc[-1], 3),
    }


def dual_window_metrics(port_ret: pd.Series, rf: pd.Series) -> dict:
    m30 = compute_metrics(port_ret, rf)
    recent = port_ret.loc[RECENT_START:]
    rf_recent = rf.loc[RECENT_START:]
    m10 = compute_metrics(recent, rf_recent)
    calmar30 = m30.get("calmar_ratio", 0) or 0
    calmar10 = m10.get("calmar_ratio", 0) or 0
    score = 0.65 * calmar10 + 0.35 * calmar30
    return {"30y": m30, "10y": m10, "weighted_score": round(score, 4)}
