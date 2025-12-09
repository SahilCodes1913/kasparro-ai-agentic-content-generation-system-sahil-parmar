# **Kasparro Applied AI – Agentic Content Generation System**  
**Author:** *Sahil Parmar*  

---

## 📌 **Overview**
This project implements a **multi-agent, modular, content-generation system** that transforms a single product dataset into:

- `faq.json` → Structured, categorized FAQs  
- `product_page.json` → Machine-readable product page  
- `comparison_page.json` → Comparison with a fictional Product B  

The system follows the **Kasparro Applied AI engineering challenge** guidelines:
- No external data used  
- Strong agent boundaries  
- Template-driven content generation  
- Structured JSON outputs  

---

## 🧠 **System Architecture**

### 🔹 **Agents & Responsibilities**
| **Agent** | **Role** |
|-----------|----------|
| **ParserAgent** | Loads & normalizes product data from `data/product.json` |
| **QuestionGeneratorAgent** | Generates ≥15 categorized Q&A using product fields |
| **TemplateEngine** | Applies templates + reusable blocks to build pages |
| **CompareAgent** | Compares GlowBoost with a fictional Product B |

---

### 🔹 **Reusable Content Blocks**
The system includes independent logic blocks such as:

- `quick_facts_block`
- `generate_benefits_block`
- `extract_usage_block`
- `safety_block`
- `price_block`
- `generate_faq_block`

Blocks ensure **separation of concerns**, **maintainability**, and **reusability**.

---

## 📂 **Project Structure**
kasparro-ai-agentic-content-generation-system-sahil-parmar/
│
├── agents/
├── blocks/
├── data/
├── templates/
├── tests/
├── docs/
├── output/
│
├── orchestrator.py
└── README.md

yaml
Copy code

---

## 🚀 **How to Run the System**

### ▶️ **1. Run the main pipeline**
```bash
python orchestrator.py
This will generate:

output/faq.json

output/product_page.json

output/comparison_page.json

### ▶️ **2. Run Tests**
bash
Copy code
python -m pytest -q
All tests should pass successfully.

📝 **Template System**
Templates are defined in:

bash
Copy code
templates/template_definitions.json
Each template references blocks, for example:
Quick facts block
Benefits block
Usage block
Safety block
Price block
This makes the system extensible and easy to modify.

📘 Documentation
Detailed documentation for the system is available in:

bash
Copy code
docs/projectdocumentation.md
It includes:

Problem Statement
Solution Overview
Scopes & Assumptions

System Design Diagram

Agent Responsibilities
