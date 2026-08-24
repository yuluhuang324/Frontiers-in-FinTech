"""Portfolio risk metrics (Layer 2, §5.3.2).

Volatility, maximum drawdown, and Sharpe ratio (Eq. 7).
"""
from __future__ import annotations
import numpy as np


def portfolio_volatility(weights: np.ndarray, cov: np.ndarray) -> float:
    """sigma_p = sqrt(w' Sigma w)."""
    return float(np.sqrt(weights @ cov @ weights))


def max_drawdown(portfolio_value: np.ndarray) -> float:
    """MDD = max_{t<=s} (V_t - V_s) / V_t."""
    peak = np.maximum.accumulate(portfolio_value)
    return float(np.max((peak - portfolio_value) / peak))


def sharpe(mean_return: float, rf: float, volatility: float) -> float:
    """SR = (mu_p - r_f) / sigma_p."""
    if volatility == 0:
        return float("nan")
    return (mean_return - rf) / volatility
