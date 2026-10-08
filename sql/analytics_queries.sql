-- 1. RFQ volume by category
SELECT product_category, COUNT(*) AS rfq_count
FROM rfqs GROUP BY product_category ORDER BY rfq_count DESC;

-- 2. High-intent share by buyer location
SELECT buyer_location,
       COUNT(*) AS total_rfqs,
       ROUND(AVG(CASE WHEN intent_label='High' THEN 1.0 ELSE 0 END)*100,2) AS high_intent_pct
FROM rfqs GROUP BY buyer_location ORDER BY high_intent_pct DESC;

-- 3. Supplier response performance
SELECT supplier_id, supplier_name, response_rate, supplier_rating
FROM suppliers ORDER BY response_rate DESC LIMIT 20;

-- 4. Average delivery time by category
SELECT primary_category, ROUND(AVG(avg_lead_time_days),2) AS avg_supplier_lead_days
FROM suppliers GROUP BY primary_category ORDER BY avg_supplier_lead_days;

-- 5. RFQ commercial value by category
SELECT product_category, ROUND(SUM(estimated_order_value),2) AS estimated_value
FROM rfqs GROUP BY product_category ORDER BY estimated_value DESC;

-- 6. Urgent RFQs
SELECT COUNT(*) AS urgent_rfqs
FROM rfqs WHERE delivery_days <= 10;

-- 7. Buyer engagement by intent
SELECT intent_label, ROUND(AVG(historical_engagement),3) AS avg_engagement
FROM rfqs GROUP BY intent_label;

-- 8. Large-quantity RFQs
SELECT rfq_id, product_category, quantity, buyer_location
FROM rfqs WHERE quantity >= 5000 ORDER BY quantity DESC LIMIT 50;

-- 9. Category-level demand
SELECT product_category, COUNT(*) AS rfq_count, ROUND(AVG(quantity),0) AS avg_quantity
FROM rfqs GROUP BY product_category ORDER BY rfq_count DESC;

-- 10. Supplier coverage by product category
SELECT product_category, COUNT(DISTINCT supplier_id) AS supplier_count
FROM supplier_products GROUP BY product_category ORDER BY supplier_count DESC;
