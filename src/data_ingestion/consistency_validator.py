"""Cross-modal consistency validator (Layer 1, §3.2.3).

Flags discrepancies between the same financial figure reported across
different disclosure channels — mirroring an audit evidence-corroboration
procedure.
"""
from __future__ import annotations


def cross_modal_check(
    value_a: float, value_b: float, materiality: float = 0.01
) -> bool:
    """Return True if the relative discrepancy exceeds the materiality
    threshold ``materiality`` (Eq. 2):

        Alert = 1[ |(v_a - v_b) / v_b| > eps_m ]
    """
    if value_b == 0:
        return False
    return abs((value_a - value_b) / value_b) > materiality
