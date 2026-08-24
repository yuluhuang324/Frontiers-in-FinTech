"""Query understanding and intent resolution (Layer 3, §5.2).

Three-level hierarchy: task classification, entity/parameter extraction,
ambiguity resolution (clarification dialogue).
"""
from __future__ import annotations
from typing import Literal

Task = Literal[
    "data_collection",
    "market_trend",
    "company_valuation",
    "portfolio_risk",
    "qa_insight",
]


def classify(query: str) -> Task:
    """Level 1: classify the query into one of five task categories."""
    raise NotImplementedError


def extract_entities(query: str) -> dict:
    """Level 2: extract companies, tickers, sectors, horizons, constraints."""
    raise NotImplementedError


def resolve_ambiguity(query: str, context: dict) -> str:
    """Level 3: produce a clarification question for underspecified queries."""
    raise NotImplementedError
