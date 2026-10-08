import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DEFAULT_WEIGHTS = {
    "product_similarity": 0.30,
    "specification_match": 0.20,
    "capacity_fit": 0.15,
    "location_fit": 0.10,
    "lead_time_fit": 0.10,
    "reliability": 0.10,
    "rating": 0.05
}

def _text(category, material, grade, dimension):
    return f"{category} {material} {grade} {dimension}".lower()

def rank_suppliers(rfq, suppliers, supplier_products, top_k=5, weights=None):
    weights = weights or DEFAULT_WEIGHTS
    sp = supplier_products.copy()
    sp["text"] = sp.apply(lambda r: _text(r.product_category,r.material,r.grade,r.dimension), axis=1)
    query = _text(rfq.get("product_category",""), rfq.get("material",""), rfq.get("grade",""), rfq.get("dimension",""))
    vect = TfidfVectorizer()
    mat = vect.fit_transform(sp["text"].tolist() + [query])
    sims = cosine_similarity(mat[-1], mat[:-1]).ravel()
    sp["product_similarity"] = sims

    merged = sp.merge(suppliers, on="supplier_id", how="left")
    merged["specification_match"] = (
        (merged["material"].fillna("").str.lower() == str(rfq.get("material","")).lower()).astype(float) * 0.5 +
        (merged["grade"].fillna("").str.lower() == str(rfq.get("grade","")).lower()).astype(float) * 0.3 +
        (merged["dimension"].fillna("").str.lower() == str(rfq.get("dimension","")).lower()).astype(float) * 0.2
    )
    qty = float(rfq.get("quantity") or 0)
    merged["capacity_fit"] = np.minimum(merged["monthly_capacity"] / max(qty,1), 2) / 2
    merged["location_fit"] = (merged["city"].str.lower() == str(rfq.get("buyer_location","")).lower()).astype(float)
    req_days = float(rfq.get("delivery_days") or 30)
    merged["lead_time_fit"] = np.clip((req_days - merged["avg_lead_time_days"] + 15) / 30, 0, 1)
    merged["reliability"] = merged["response_rate"]
    merged["rating"] = merged["supplier_rating"] / 5.0
    merged["match_score"] = sum(weights[k] * merged[k] for k in weights) * 100
    merged["missing_or_risk"] = merged.apply(
        lambda r: "Longer lead time than requested" if r["avg_lead_time_days"] > req_days
        else ("Low response rate" if r["response_rate"] < 0.60 else "No major risk identified"), axis=1
    )
    best = merged.sort_values("match_score", ascending=False).drop_duplicates("supplier_id").head(top_k).copy()
    return best[["supplier_id","supplier_name","city","product_category","match_score",
                 "product_similarity","specification_match","capacity_fit","location_fit",
                 "lead_time_fit","reliability","supplier_rating","avg_lead_time_days",
                 "missing_or_risk"]]

def prioritize_lead(rfq, intent_probability):
    qty = float(rfq.get("quantity") or 0)
    delivery = float(rfq.get("delivery_days") or 30)
    engagement = float(rfq.get("historical_engagement") or 0)
    completeness = sum(bool(rfq.get(k)) for k in ["product_category","material","grade","dimension","quantity","buyer_location","delivery_days"]) / 7
    qty_score = min(qty / 5000, 1)
    urgency_score = 1 if delivery <= 10 else (0.7 if delivery <= 20 else 0.4)
    score = 100*(0.35*intent_probability + 0.20*qty_score + 0.15*urgency_score + 0.15*engagement + 0.15*completeness)
    priority = "HIGH" if score >= 70 else ("MEDIUM" if score >= 45 else "LOW")
    reasons = []
    if intent_probability >= .65: reasons.append("high predicted purchase intent")
    if qty >= 3000: reasons.append("large requested quantity")
    if delivery <= 10: reasons.append("short delivery requirement")
    if completeness >= .85: reasons.append("well-specified RFQ")
    if not reasons: reasons.append("limited commercial urgency/signals")
    return round(score,1), priority, reasons
