# **Kasparro Applied AI – Agentic Content Generation System**  
**Author:** *Sahil Parmar*  

---

## 📌 **Overview**
This project implements a **multi-agent, modular content-generation system** designed for the **Kasparro Applied AI Challenge**.  
The system transforms a single product dataset into structured, machine-readable JSON outputs:

- `faq.json` → Categorized FAQs  
- `product_page.json` → Product page with reusable blocks  
- `comparison_page.json` → Comparison with a fictional Product B  

This system demonstrates:
- Strong agent boundaries  
- Template-driven generation  
- Reusable content blocks  
- Clean JSON output formatting  
- No use of external knowledge  

---

## 🧠 **System Architecture**

### 🔹 **Agents & Responsibilities**
| **Agent** | **Role** |
|-----------|----------|
| **ParserAgent** | Loads & normalizes product data from `data/product.json` |
| **QuestionGeneratorAgent** | Generates ≥15 categorized Q&A items |
| **TemplateEngine** | Uses templates + blocks to build product & FAQ pages |
| **CompareAgent** | Compares GlowBoost with a fictional Product B |

---

## 🔹 **Reusable Content Blocks**
The system includes reusable logic blocks such as:

- `quick_facts_block`
- `generate_benefits_block`
- `extract_usage_block`
- `safety_block`
- `price_block`
- `generate_faq_block`

Blocks help maintain **separation of concerns**, **scalability**, and **clean logic flow**.

---

## 📂 **Project Structure**

```text
kasparro-ai-agentic-content-generation-system-sahil-parmar/
│
├── agents/
│   ├── parser_agent.py
│   ├── question_generator_agent.py
│   ├── template_engine.py
│   └── compare_agent.py
│
├── blocks/
│   ├── quick_facts_block.py
│   ├── generate_benefits_block.py
│   ├── extract_usage_block.py
│   ├── safety_block.py
│   ├── price_block.py
│   └── generate_faq_block.py
│
├── data/
│   └── product.json
│
├── templates/
│   └── template_definitions.json
│
├── tests/
│   ├── test_parser.py
│   └── test_template.py
│
├── docs/
│   └── projectdocumentation.md
│
├── output/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── orchestrator.py
└── README.md
