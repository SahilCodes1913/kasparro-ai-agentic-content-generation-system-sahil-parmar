Kasparro Applied AI – Agentic Content Generation System

Author: Sahil Parmar

🎯 Overview

This project implements a multi-agent content generation system that processes a single product dataset and generates:

faq.json → Machine-readable structured FAQs

product_page.json → Structured product page with reusable blocks

comparison_page.json → Comparison against a fictional Product B

The system demonstrates modular engineering, template-driven content generation, and clean agent boundaries — exactly as required in the Applied AI challenge.

🧩 System Architecture
Agents Used
Agent	Responsibility
ParserAgent	Reads & normalizes data/product.json
QuestionGeneratorAgent	Produces categorized Q&A (≥15 questions)
TemplateEngine	Builds structured pages from templates + blocks
CompareAgent	Compares GlowBoost with a fictional Product B
Content Blocks

quick_facts_block

generate_benefits_block

extract_usage_block

safety_block

price_block

generate_faq_block

These ensure reusability and separation of concerns.

📂 Project Structure
agents/
blocks/
data/
templates/
output/
tests/
docs/
orchestrator.py
README.md

🚀 How to Run
1) Run the orchestration pipeline
python orchestrator.py


This generates:

output/faq.json

output/product_page.json

output/comparison_page.json

2) Run Tests
python -m pytest -q


All tests should pass.

📝 Templates

Templates are defined in:

templates/template_definitions.json


Each section references a block, making the system extensible and easy to modify.

📘 Documentation

Full engineering documentation is inside:

docs/projectdocumentation.md


It includes:

Problem statement

Solution overview

Scopes & assumptions

System design

Agent boundaries
