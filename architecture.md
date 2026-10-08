# Architecture

```text
Buyer RFQ
   |
   v
Requirement Extraction
   |
   +----> Validation / Missing fields
   |
   v
Intent Classifier --------> Lead Priority
   |
   v
Candidate Supplier Retrieval
   |
   v
Hybrid Matching Engine
   |       |
   |       +--> Product/text similarity
   |       +--> Specification match
   |       +--> Capacity fit
   |       +--> Location fit
   |       +--> Lead-time fit
   |       +--> Reliability/rating
   v
Supplier Ranking
   |
   v
Explainable Recommendations
   |
   v
Sales Dashboard / Human Feedback
   |
   v
Analytics + Future Model Improvement
```
