from agents.parser_agent import parse_product
from agents.question_generator_agent import generate_questions
from agents.template_engine import render_templates
import json, pathlib
def test_render_templates():
    product = json.loads(pathlib.Path("data/product.json").read_text(encoding="utf8"))
    normalized = parse_product(product)
    faqs = generate_questions(normalized)
    out = render_templates(normalized, faqs, "templates/template_definitions.json")
    assert "product_page" in out and "faq" in out
    assert out["faq"]["product"] == normalized["product_name"]
