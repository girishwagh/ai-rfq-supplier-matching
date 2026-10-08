CREATE TABLE IF NOT EXISTS buyers (
    buyer_id TEXT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS rfqs (
    rfq_id TEXT PRIMARY KEY,
    buyer_id TEXT,
    raw_rfq_text TEXT,
    product_category TEXT,
    material TEXT,
    grade TEXT,
    dimension TEXT,
    quantity INTEGER,
    buyer_location TEXT,
    delivery_days INTEGER,
    intent_label TEXT,
    estimated_order_value REAL
);
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT,
    city TEXT,
    state TEXT,
    primary_category TEXT,
    max_monthly_capacity INTEGER,
    avg_lead_time_days INTEGER,
    response_rate REAL,
    supplier_rating REAL
);
CREATE TABLE IF NOT EXISTS supplier_products (
    supplier_id TEXT,
    product_category TEXT,
    material TEXT,
    grade TEXT,
    dimension TEXT,
    monthly_capacity INTEGER
);
CREATE TABLE IF NOT EXISTS recommendations (
    rfq_id TEXT,
    supplier_id TEXT,
    match_score REAL,
    rank_position INTEGER
);
CREATE TABLE IF NOT EXISTS lead_scores (
    rfq_id TEXT,
    priority_score REAL,
    priority TEXT
);
