import json
from agents.parser_agent import parse_product
from agents.question_generator_agent import generate_questions
from agents.template_engine import render_templates
from agents.compare_agent import compare_products
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "product.json"
TEMPLATES = ROOT / "templates" / "template_definitions.json"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

def main():
    product = json.loads(DATA.read_text(encoding="utf8"))
    normalized = parse_product(product)
    # generate questions (≥15)
    faqs = generate_questions(normalized)
    # render product page and faq using templates and blocks
    rendered = render_templates(normalized, faqs, TEMPLATES)
    # compare
    comparison = compare_products(normalized)
    # write outputs
    (OUT / "faq.json").write_text(json.dumps(rendered["faq"], indent=2, ensure_ascii=False), encoding="utf8")
    (OUT / "product_page.json").write_text(json.dumps(rendered["product_page"], indent=2, ensure_ascii=False), encoding="utf8")
    (OUT / "comparison_page.json").write_text(json.dumps(comparison, indent=2, ensure_ascii=False), encoding="utf8")
    print("Wrote output/faq.json, output/product_page.json, output/comparison_page.json")

if __name__ == "__main__":
    main()
