# Product Requirements Document

## Problem
B2B marketplaces receive high volumes of unstructured buyer enquiries. Sales or marketplace teams may need to interpret the request, identify relevant supplier capabilities and decide which leads deserve immediate attention.

## Personas
1. Buyer — wants relevant suppliers quickly.
2. Sales/Lead Manager — wants high-intent RFQs prioritized.
3. Product Team — wants measurable improvements in matching and conversion workflows.

## Goals
- Convert unstructured RFQs into structured requirements.
- Prioritize commercially valuable/urgent leads.
- Rank relevant suppliers transparently.
- Reduce manual screening effort.
- Capture human feedback for continuous improvement.

## Non-goals
- Autonomous quotation negotiation.
- Automatic supplier onboarding.
- Real payment/order execution.
- Claims about actual IndiaMART performance.

## MVP
1. RFQ parsing
2. Intent scoring
3. Supplier matching/ranking
4. Explainability
5. Lead dashboard
6. SQL analytics

## User stories
- As a sales executive, I want high-intent RFQs prioritized so I can focus on likely business opportunities.
- As a buyer, I want relevant suppliers ranked so I can compare options quickly.
- As a sales executive, I want to understand why a supplier was recommended so I can validate the recommendation.
- As a product manager, I want match-quality metrics so I can identify catalogue gaps.

## Acceptance criteria
- Given a valid RFQ, when submitted, structured fields are displayed.
- Given an RFQ with enough information, the system returns a priority score.
- Given supplier data, the system returns ranked candidates.
- Every recommendation includes an explanation and risk note.
- Missing information does not crash the workflow.

## Requirements
Functional: extraction, classification, matching, ranking, explanation, feedback.
Non-functional: reproducibility, transparency, low latency for demo-scale data, safe handling of credentials.

## Success metrics
North Star: successful RFQ-to-qualified-supplier connection rate.
Supporting: Top-K precision, high-intent precision, response time, supplier response rate, recommendation acceptance.
