# `src/` — System Reference Architecture (scaffolding)

> **Status: architectural scaffolding.** The modules in this directory are
> **stubs** that encode Frontiers in FinTech's three-layer design (paper, Sections 3–5).
> They document the intended interfaces and map each component to the
> corresponding equation/section in the manuscript. They are **not** a runnable
> implementation; method bodies raise `NotImplementedError`. A production
> release of the trained weights and full pipeline is planned.

| Paper layer | Package | Key modules |
|---|---|---|
| Layer 1 — Multimodal Data Ingestion (Innovation I, §3) | `data_ingestion/` | `vlm_encoder`, `field_extractor`, `consistency_validator` |
| Layer 2 — Financial Intelligence (Innovation II, §4) | `intelligence/` | `valuation`, `market_trend`, `risk`, `training/{pretrain,finetune}` |
| Layer 3 — NL Decision Pipeline (Innovation III, §5) | `decision/` | `nl_query_parser`, `dag_scheduler`, `portfolio`, `report` |

Equation references below use the numbering in `paper/Frontiers_in_FinTech.tex`.
