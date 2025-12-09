def generate_benefits_block(product):
    return [{"title": b, "explanation": f"{b} — {product['product_name']} helps with {b.lower()}."} for b in product["benefits"]]
