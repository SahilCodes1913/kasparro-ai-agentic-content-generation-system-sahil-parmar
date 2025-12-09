import json
from pathlib import Path
from blocks.quick_facts_block import quick_facts_block
from blocks.generate_benefits_block import generate_benefits_block
from blocks.extract_usage_block import extract_usage_block
from blocks.safety_block import safety_block
from blocks.price_block import price_block
from blocks.generate_faq_block import generate_faq_block

BLOCK_MAP = {
    "quick_facts_block": quick_facts_block,
    "generate_benefits_block": generate_benefits_block,
    "extract_usage_block": extract_usage_block,
    "safety_block": safety_block,
    "price_block": price_block,
    "generate_faq_block": generate_faq_block
}

def render_templates(product, faqs, template_path):
    templates = json.loads(Path(template_path).read_text(encoding="utf8"))
    out = {}
    # product page
    tp = templates["product_page"]
    product_page = {"title": tp.get("title","").replace("{{product_name}}", product["product_name"]), "sections": {}}
    for sec in tp["sections"]:
        block_fn = BLOCK_MAP[sec["block"]]
        product_page["sections"][sec["id"]] = block_fn(product)
    out["product_page"] = product_page
    # faq
    faq_block_fn = BLOCK_MAP["generate_faq_block"]
    out["faq"] = faq_block_fn(product, faqs)
    return out
