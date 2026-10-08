# Model Evaluation

## Intent classifier
- Model: TF-IDF (1-2 grams) + Logistic Regression
- Train/test split: 80/20, stratified
- Accuracy: **56.20%**
- Macro F1: **0.542**

The synthetic labels are generated from observable commercial signals such as quantity, delivery requirement, urgency, engagement and estimated order value. This is intentional for a reproducible prototype, but it is **not evidence of real-world IndiaMART performance**.

## Product interpretation
For a production system, intent labels should come from historical outcomes or human-reviewed annotations. Precision/recall by class should be monitored because false high-priority leads can waste sales capacity.

## Matching evaluation
The supplier matching engine is designed for ranking evaluation using Precision@K, Recall@K and NDCG@K. Because this project uses synthetic supplier data, production-quality relevance labels are not claimed.
