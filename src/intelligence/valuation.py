"""Valuation engine (Layer 2, §4.3.2).

Encodes the valuation-model library: DCF, P/E, P/B, P/S, EV/EBITDA, Residual
Income. The model auto-selects the method by entity type / life-cycle stage.
"""
from __future__ import annotations
from typing import Literal

Method = Literal["DCF", "PE", "PB", "PS", "EV/EBITDA", "RI"]


def dcf(
    fcff: list[float], wacc: float, terminal_growth: float, shares: float
) -> float:
    """Discounted cash flow (FCFF discounted at WACC, Gordon terminal)."""
    raise NotImplementedError


def multiple(market_cap: float, metric: float) -> float:
    """Generic valuation multiple (P/E, P/B, P/S, EV/EBITDA)."""
    if metric == 0:
        return float("nan")
    return market_cap / metric


def residual_income(
    book_value: float, earnings: float, cost_of_equity: float, b: float
) -> float:
    """Residual-income valuation anchored on book value + abnormal earnings."""
    raise NotImplementedError
