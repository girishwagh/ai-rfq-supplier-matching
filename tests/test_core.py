from src.preprocessing import extract_requirements
from src.matching import prioritize_lead

def test_extraction():
    x = extract_requirements("Need 5000 stainless steel brackets, SS304, 5 mm, Pune within 15 days")
    assert x["quantity"] == 5000
    assert x["buyer_location"] == "Pune"
    assert x["delivery_days"] == 15

def test_priority():
    score, priority, reasons = prioritize_lead({
        "quantity":5000,"delivery_days":7,"historical_engagement":.8,
        "product_category":"Steel Brackets","material":"Stainless Steel",
        "grade":"SS304","dimension":"5 mm","buyer_location":"Pune"
    }, .85)
    assert score > 70
    assert priority == "HIGH"
    assert len(reasons) > 0
