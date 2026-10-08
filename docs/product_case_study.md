# Product Case Study

## Situation
A B2B marketplace must connect buyer requirements with relevant suppliers efficiently.

## Problem
Natural-language RFQs contain product specifications, quantity, location and urgency in inconsistent formats. Manual interpretation can slow response prioritization.

## Insight
The workflow can be decomposed into deterministic constraints, ML-based language understanding and transparent ranking.

## Solution
An AI-assisted RFQ intelligence platform that extracts requirements, predicts buyer intent, ranks suppliers and explains recommendations.

## Key trade-offs
- Rules vs ML: use rules for hard constraints; ML for language/similarity.
- Accuracy vs latency: start with lightweight models; introduce embeddings at larger scale.
- Automation vs human review: keep sales override and feedback.
- Relevance vs catalogue coverage: expose uncertainty instead of forcing a recommendation.

## MVP
RFQ extraction, intent scoring, supplier ranking, explanation and sales dashboard.

## Future roadmap
Phase 2: embeddings, feedback learning, supplier response prediction, better taxonomy.
Phase 3: experimentation platform, online learning, recommendation personalization, multilingual RFQ understanding.
