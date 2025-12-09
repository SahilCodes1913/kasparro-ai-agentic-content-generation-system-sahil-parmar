from agents.parser_agent import parse_product
def test_parse_minimal():
    raw={"product_name":"X","concentration":"10%","skin_type":["A"],"key_ingredients":["I"],"benefits":["B"],"how_to_use":"u","side_effects":"s","price":"₹100"}
    out = parse_product(raw)
    assert out["product_name"]=="X"
    assert isinstance(out["key_ingredients"], list)
