from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class ProductModel:
    product_name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str

def parse_product(raw: Dict[str, Any]) -> Dict[str, Any]:
    # normalize simple types
    pm = ProductModel(
        product_name=str(raw.get("product_name","")).strip(),
        concentration=str(raw.get("concentration","")).strip(),
        skin_type=[s.strip() for s in raw.get("skin_type",[])],
        key_ingredients=[s.strip() for s in raw.get("key_ingredients",[])],
        benefits=[s.strip() for s in raw.get("benefits",[])],
        how_to_use=str(raw.get("how_to_use","")).strip(),
        side_effects=str(raw.get("side_effects","")).strip(),
        price=str(raw.get("price","")).strip()
    )
    return asdict(pm)
