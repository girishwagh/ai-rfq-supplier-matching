# Interview Guide

## 60-second pitch
I built an independent AI-powered B2B marketplace prototype inspired by a problem I encountered while working on RFQs. The system takes an unstructured buyer requirement, extracts key specifications, predicts buyer intent, ranks suppliers using a hybrid matching model, and prioritizes the lead for sales action. I deliberately used rules for hard constraints and ML for language and similarity, because I wanted the product to be explainable rather than a black box. I also added SQL analytics, product KPIs and a human feedback loop. The project helped me combine my engineering/RFQ experience with my MBA Business Analytics learning and think through the problem as both a product manager and an analyst.

## Likely questions
1. Why this problem? — It connects my RFQ exposure with B2B marketplace matching.
2. Why ML? — Natural-language requirements are variable; ML captures patterns that rules alone miss.
3. Why not LLM-only? — Cost, latency, reproducibility and explainability; use LLM selectively for extraction.
4. How is matching calculated? — Weighted combination of semantic similarity and structured business constraints.
5. How evaluate matching? — Precision@K/Recall@K/NDCG with labelled or human-reviewed relevance data in production.
6. What is the North Star? — Successful RFQ-to-qualified-supplier connection rate.
7. What if no supplier matches? — Return no strong recommendation, surface gaps and ask for missing requirements.
8. How scale? — Candidate retrieval first, then reranking; cache embeddings; partition indexes; monitor latency.
9. Biggest limitation? — Synthetic data is not representative of real marketplace behavior.
10. What would you build next? — Human feedback loop, better taxonomy/entity extraction and online experiments.
