# kasparro-ai-agentic-content-generation-system-sahil-parmar

## Goal
Generate 3 machine-readable JSON pages for GlowBoost Vitamin C Serum using an agentic pipeline.

## Requirements met
- Parser, Question generator, Template engine, Compare agent
- Templates + reusable blocks
- Outputs: faq.json, product_page.json, comparison_page.json

## Run locally
1. Create a repo folder and paste the files as provided (this zip contains them).
2. (Optional) create a venv: `python -m venv venv && source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` on Windows.
3. Run:
   ```
   python orchestrator.py
   ```
4. Outputs will be in `output/`:
   - output/faq.json
   - output/product_page.json
   - output/comparison_page.json

## Tests
Run:
```
pip install pytest
pytest -q
```

## Notes
This project intentionally uses only Python stdlib to keep setup trivial. It follows the assignment constraints: modular agents, templates, JSON output.
