"""Stage 2: institution-specific fine-tuning (§4.3.1).

Parameter-efficient adaptation via LoRA + Prompt Tuning, preserving
broad financial knowledge while acquiring institution-specific logic.
"""
from __future__ import annotations
from typing import Any


def lora_finetune(model: Any, train_data: Any, config: dict | None = None) -> Any:
    """Adapt ``model`` to institution-specific data with LoRA adapters."""
    raise NotImplementedError
