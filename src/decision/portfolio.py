"""MPT-based portfolio optimizer (Layer 3, §5.3.1).

Mean-variance optimization (Eq. 5):

    min_w  w' Sigma w   s.t.  w'mu >= mu*,  w'1 = 1,  w_i >= 0
"""
from __future__ import annotations
import numpy as np


def mean_variance(
    mu: np.ndarray, cov: np.ndarray, target_return: float
) -> np.ndarray:
    """Solve the Markowitz problem for portfolio weights ``w``."""
    raise NotImplementedError
