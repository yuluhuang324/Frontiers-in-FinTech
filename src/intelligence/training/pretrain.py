"""Stage 1: large-scale financial domain pre-training (§4.2).

Multi-task objective (Eq. 3):

    L_pre = lambda1*L_LM + lambda2*L_ITM + lambda3*L_ITG + lambda4*L_fin
"""
from __future__ import annotations
import torch


def pretrain_loss(
    lm_loss: torch.Tensor,
    itm_loss: torch.Tensor,
    itg_loss: torch.Tensor,
    fin_loss: torch.Tensor,
    lambdas: tuple[float, float, float, float] = (1.0, 0.5, 0.5, 1.0),
) -> torch.Tensor:
    l1, l2, l3, l4 = lambdas
    return l1 * lm_loss + l2 * itm_loss + l3 * itg_loss + l4 * fin_loss
