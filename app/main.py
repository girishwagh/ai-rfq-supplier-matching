import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
import pandas as pd
from src.preprocessing import extract_requirements
from src.models import load_intent_model
from src.matching import rank_suppliers, prioritize_lead

st.set_page_config(page_title="RFQ Intelligence", page_icon="📦", layout="wide")

@st.cache_data
def load_data():
    rfqs = pd.read_csv("data/rfqs.csv")
    suppliers = pd.read_csv("data/suppliers.csv")
    sp = pd.read_csv("data/supplier_products.csv")
    return rfqs, suppliers, sp

@st.cache_resource
def load_model():
    try:
        return load_intent_model("models/intent_model.joblib")
    except Exception:
        return None

rfqs, suppliers, sp = load_data()
model = load_model()

st.title("📦 AI-Powered RFQ Intelligence")
st.caption("Independent B2B marketplace prototype | Synthetic data | AI-assisted supplier matching & lead prioritization")

example = "Need 5000 stainless steel brackets, SS304, 5 mm, for industrial use. Delivery required in Pune within 15 days. Please share quotation."
rfq_text = st.text_area("Enter a buyer RFQ", value=example, height=120)

if st.button("Analyze RFQ", type="primary"):
    req = extract_requirements(rfq_text)
    req["raw_rfq_text"] = rfq_text

    st.subheader("1. Extracted requirements")
    req_df = pd.DataFrame([req]).T.reset_index()
    req_df.columns = ["Field","Value"]
    st.dataframe(req_df, use_container_width=True, hide_index=True)

    if model:
        probs = model.predict_proba([rfq_text])[0]
        labels = model.classes_
        prob_map = dict(zip(labels, probs))
        intent = model.predict([rfq_text])[0]
        intent_prob = float(prob_map.get(intent, max(probs)))
    else:
        # Demo fallback based on extracted fields
        qty = req.get("quantity") or 0
        days = req.get("delivery_days") or 30
        intent_prob = min(.95, .35 + (.25 if qty >= 3000 else .10) + (.20 if days <= 10 else .05))
        intent = "High" if intent_prob >= .65 else ("Medium" if intent_prob >= .45 else "Low")

    score, priority, reasons = prioritize_lead(req, intent_prob)
    c1,c2,c3 = st.columns(3)
    c1.metric("Buyer intent", intent, f"{intent_prob:.0%} confidence")
    c2.metric("Lead priority", priority)
    c3.metric("Priority score", f"{score}/100")

    st.subheader("2. Why was this lead prioritized?")
    for r in reasons:
        st.write("•", r)

    st.subheader("3. Recommended suppliers")
    try:
        results = rank_suppliers(req, suppliers, sp, top_k=5)
        display = results.copy()
        display["match_score"] = display["match_score"].round(1).astype(str) + "%"
        display["supplier_rating"] = display["supplier_rating"].round(1)
        st.dataframe(display, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(f"Matching engine error: {e}")

    st.subheader("4. Recommendation explanation")
    if 'results' in locals() and len(results):
        top = results.iloc[0]
        st.info(
            f"**{top['supplier_name']}** is ranked #1 because it has a "
            f"**{top['match_score']:.1f}% overall match**, with product similarity of "
            f"{top['product_similarity']:.0%}, capacity fit of {top['capacity_fit']:.0%}, "
            f"location fit of {top['location_fit']:.0%}, and lead-time fit of "
            f"{top['lead_time_fit']:.0%}. Risk note: {top['missing_or_risk']}."
        )

st.divider()
st.subheader("Marketplace analytics")
m1,m2,m3,m4 = st.columns(4)
m1.metric("Synthetic RFQs", f"{len(rfqs):,}")
m2.metric("High-intent RFQs", f"{(rfqs.intent_label=='High').mean():.1%}")
m3.metric("Suppliers", f"{len(suppliers):,}")
m4.metric("Supplier catalogue rows", f"{len(sp):,}")

st.caption("Disclaimer: All supplier, RFQ, performance and impact figures are synthetic and created only for this portfolio prototype. They are not IndiaMART data.")
