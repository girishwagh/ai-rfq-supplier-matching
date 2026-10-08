import re
import pandas as pd

FIELDS = ["product_category","material","grade","dimension","quantity","buyer_location","delivery_days"]

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text).strip().lower())

def extract_requirements(text: str) -> dict:
    """Lightweight deterministic parser for the demo; can be replaced by an LLM parser."""
    t = normalize_text(text)
    result = {k: None for k in FIELDS}
    categories = ["industrial pumps","ball valves","steel brackets","conveyor belts",
                  "electric motors","hydraulic cylinders","gearboxes","sheet metal parts"]
    materials = ["stainless steel","mild steel","carbon steel","cast iron","rubber","pu","aluminium","steel"]
    cities = ["pune","mumbai","nashik","delhi","ahmedabad","bengaluru","hyderabad","chennai","kolkata","nagpur"]
    grades = ["ss304","ss316","ms","cs","ie2","ie3","grade a","food grade","helical","worm"]
    dimensions = ["500 mm","800 mm","1000 mm","1 inch","2 inch","3 inch","3 mm","5 mm","8 mm",
                  "10 mm","50 mm","100 mm","150 mm","5 hp","10 hp","20 hp","25 hp","2 hp"]
    for c in categories:
        if c in t: result["product_category"] = c.title()
    for m in materials:
        if m in t: result["material"] = m.title()
    for g in grades:
        if g in t: result["grade"] = g.upper()
    for d in dimensions:
        if d in t: result["dimension"] = d.upper() if "hp" in d else d
    q = re.search(r"(\d[\d,]*)\s*(?:units|pcs|pieces|nos|numbers)?", t)
    if q:
        result["quantity"] = int(q.group(1).replace(",",""))
    for c in cities:
        if c in t: result["buyer_location"] = c.title()
    d = re.search(r"(?:within|in|required in|required by)\s+(\d+)\s*days?", t)
    if d: result["delivery_days"] = int(d.group(1))
    return result

def feature_text(df):
    cols = ["product_category","material","grade","dimension","application","urgency"]
    return df[cols].fillna("").astype(str).agg(" ".join, axis=1)
