# Kasparro AI Agentic Content Generation System
Repo: kasparro-ai-agentic-content-generation-system-sahil-parmar

## Problem Statement
Design a modular agentic automation system that takes a small product dataset and automatically generates structured, machine-readable content pages (FAQ, Product Page, Comparison). Use only the provided product data: GlowBoost Vitamin C Serum. No external facts allowed. 

## Solution Overview
We implement a small orchestration pipeline composed of independent agents:
- ParserAgent: reads/normalizes product JSON.
- QuestionGeneratorAgent: creates categorized Q&A items.
- TemplateEngineAgent: consumes templates and content blocks to produce structured JSON pages.
- CompareAgent: compares product against a fictional Product B.

All agents have single responsibility, no hidden global state, and return plain Python data structures. Templates are JSON definitions that reference "blocks". Blocks are small pure functions that extract or render a particular piece of content.

## Scopes & Assumptions
- Input is exactly the provided product JSON schema. No external lookups or added facts about GlowBoost beyond the given fields.
- Product B (for comparison) is fictional and created locally; it follows the same schema.
- Output pages are machine-readable JSON files: `faq.json`, `product_page.json`, `comparison_page.json`.
- This submission focuses on system design, modularity, and JSON correctness (no UI, no deployment).

## System Design
Flow (simple DAG):
1. orchestrator.py loads `data/product.json`.
2. ParserAgent -> produce normalized product model.
3. QuestionGeneratorAgent -> produce Q&A items.
4. TemplateEngine -> render product_page & faq using blocks.
5. CompareAgent -> build comparison_page.
6. orchestrator writes JSON files to `output/`.

Agent boundaries:
- Each agent is a module with a single public `run(...)` function.
- Blocks are pure helper functions located under `blocks/`.

## Files & Structure
- `orchestrator.py`
- `agents/parser_agent.py`
- `agents/question_generator_agent.py`
- `agents/template_engine.py`
- `agents/compare_agent.py`
- `blocks/*.py`
- `templates/template_definitions.json`
- `data/product.json`
- `output/*.json`
- `docs/projectdocumentation.md`

## How this meets evaluation criteria
- Clear agent boundaries and single responsibility (Agentic System Design).
- Reusable blocks and template engine show content system engineering.
- Output is machine-readable JSON with a clear mapping from data → logic → output.
