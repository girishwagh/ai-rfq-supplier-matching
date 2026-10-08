# AI-Powered RFQ-to-Supplier Matching & Lead Prioritization

**Independent portfolio prototype for an IndiaMART Assistant Product Manager – Product & Tech application.**

## One-line pitch
An AI-assisted B2B marketplace workflow that converts unstructured buyer RFQs into structured requirements, predicts buyer intent, ranks relevant suppliers and prioritizes leads for sales action.

## Why this project?
B2B RFQs are often unstructured and require manual interpretation before a buyer can be connected with relevant suppliers. This prototype explores how AI/ML + structured product workflows can reduce screening effort while keeping humans in the loop.

## Product flow
`Buyer RFQ → Requirement extraction → Intent prediction → Supplier candidate matching → Ranking → Explainable recommendation → Lead prioritization → Sales action`

## What is implemented?
- Synthetic dataset with 5,000 RFQs, 1,000 suppliers and supplier-product mappings
- NLP intent classifier using TF-IDF + Logistic Regression
- Hybrid supplier matching using text similarity + structured attributes
- Explainable supplier ranking
- Lead prioritization score
- SQL analytics schema + 10 business queries
- Streamlit product prototype
- Product/technical documentation

## Tech stack
Python, Pandas, NumPy, Scikit-learn, SQLite/SQL, Streamlit, Plotly, Git/GitHub.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m src.train
streamlit run app/main.py
```

## Dataset
All RFQs, suppliers and performance attributes are **synthetic**. They are not IndiaMART data and must not be represented as such.

## ML evaluation
Run `python -m src.train` to generate the intent model and evaluation output. The project intentionally evaluates precision/recall/F1 rather than relying on accuracy alone.

## Product metrics
North Star: successful RFQ-to-qualified-supplier connection rate.

Supporting metrics:
- Top-K supplier match precision
- High-intent identification precision
- RFQ processing time
- Supplier response rate
- Recommendation acceptance rate
- RFQ-to-response time

Guardrails:
- False high-priority leads
- Poor supplier recommendations
- Model confidence
- Latency

## Limitations
The synthetic dataset does not reproduce real marketplace behavior. Supplier recommendations are a prototype and require human review. A production system would need real interaction data, a robust taxonomy, entity resolution, privacy controls, offline/online evaluation and continuous monitoring.

## Repository structure
See `docs/` for the PRD, JD mapping, product case study and interview guide.

## Disclaimer
This is an independent portfolio project. It does not use confidential information or claim any relationship with IndiaMART.
