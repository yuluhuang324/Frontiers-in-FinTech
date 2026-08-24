# System Architecture

Frontiers in FinTech is organized as three integrated layers (paper, §6; see
[`paper/figures/architecture.png`](../paper/figures/architecture.png)):

1. **Multimodal Data Ingestion (Innovation I, §3)** — a VLM encoder with a
   financial field extractor and a cross-modal consistency validator parses
   PDF / Excel / chart / scanned-policy documents into a 120-field GAAP/IFRS
   schema (Eq. 1–2).
2. **Financial Intelligence (Innovation II, §4)** — a two-stage trained LLM
   (large-scale pre-training, Eq. 3; institution-specific LoRA fine-tuning)
   drives valuation, market-trend, and risk modules.
3. **NL Decision Pipeline (Innovation III, §5)** — a natural-language parser
   builds a task DAG (Eq. 4), runs Markowitz portfolio optimization (Eq. 5),
   monitors risk (Eq. 7), and returns a structured report over multi-turn
   dialogue.

The `src/` package mirrors this layering one-to-one; see `src/README.md`.
