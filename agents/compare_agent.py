def compare_products(product):
    # create a fictional Product B
    product_b = {
        "product_name":"RadiantC Booster",
        "concentration":"12% Vitamin C",
        "key_ingredients":["Vitamin C", "Niacinamide"],
        "benefits":["Brightening","Hydration"],
        "price":"₹799"
    }
    # compare price
    def parse_price(p):
        return int(''.join(ch for ch in p if ch.isdigit()) or 0)
    lhs_price = parse_price(product["price"])
    rhs_price = parse_price(product_b["price"])
    winner = "GlowBoost" if lhs_price <= rhs_price else product_b["product_name"]
    common_ingredients = list(set(product["key_ingredients"]).intersection(set(product_b["key_ingredients"])))
    comp = {
        "lhs": product["product_name"],
        "rhs": product_b["product_name"],
        "comparison": [
            {"aspect":"price","lhs":product["price"],"rhs":product_b["price"],"cheaper":("lhs" if lhs_price < rhs_price else "tie" if lhs_price==rhs_price else "rhs")},
            {"aspect":"ingredients_overlap","common":common_ingredients},
            {"aspect":"concentration","lhs":product["concentration"],"rhs":product_b["concentration"]},
            {"aspect":"summary","verdict": f"{winner} is better priced based on listed price."}
        ]
    }
    return comp
