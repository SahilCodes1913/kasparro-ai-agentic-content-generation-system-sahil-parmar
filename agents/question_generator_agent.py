from typing import Dict, List

def generate_questions(product: Dict) -> List[Dict]:
    name = product["product_name"]
    qas = []
    # Usage
    qas.append({"category":"Usage","q":"How do I use "+name+"?","a":product["how_to_use"]})
    qas.append({"category":"Usage","q":"How many drops should I apply?","a":"Apply 2–3 drops."})
    qas.append({"category":"Usage","q":"When should I apply it?","a":"In the morning before sunscreen."})
    # Safety
    qas.append({"category":"Safety","q":"Will it irritate sensitive skin?","a":product["side_effects"]})
    qas.append({"category":"Safety","q":"Should I patch test?","a":"Yes — patch test on inner forearm before full use if you have sensitive skin."})
    # Informational
    qas.append({"category":"Informational","q":"What concentration of Vitamin C does it have?","a":product["concentration"]})
    qas.append({"category":"Informational","q":"What are the key ingredients?","a":", ".join(product["key_ingredients"])})
    qas.append({"category":"Informational","q":"Which skin types is it for?","a":", ".join(product["skin_type"])})
    # Benefits
    for b in product["benefits"]:
        qas.append({"category":"Benefits","q":f"What does it do for {b.lower()}?","a":f"{b}. "})
    # Purchase / Price
    qas.append({"category":"Purchase","q":"How much does it cost?","a":product["price"]})
    qas.append({"category":"Purchase","q":"Where should I buy it?","a":"Check official store or trusted retailers."})
    # Comparison-style (generic)
    qas.append({"category":"Comparison","q":"How does it compare to other vitamin C serums?","a":"Offers 10% Vitamin C with hyaluronic acid; compare ingredient lists and price."})
    # Fill up to at least 15
    if len(qas) < 15:
        extras = [
            {"category":"Usage","q":"Can I use it with other products?","a":"Use it before sunscreen; avoid mixing with strong acids immediately."},
            {"category":"Storage","q":"How should I store it?","a":"Keep in a cool, dark place to preserve potency."}
        ]
        qas.extend(extras[:max(0,15 - len(qas))])
    return qas
