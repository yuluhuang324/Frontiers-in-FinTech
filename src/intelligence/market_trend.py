"""Market trend analyzer (Layer 2, §4).

Technical indicators for trend / momentum analysis.
"""
from __future__ import annotations
import numpy as np


def macd(close: np.ndarray, fast: int = 12, slow: int = 26, signal: int = 9):
    """MACD line and signal line."""
    raise NotImplementedError


def rsi(close: np.ndarray, window: int = 14) -> np.ndarray:
    """Relative Strength Index."""
    raise NotImplementedError
