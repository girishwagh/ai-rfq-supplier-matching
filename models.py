from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

def train_intent_model(df, out_path="models/intent_model.joblib"):
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=2)),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    pipe.fit(df["raw_rfq_text"], df["intent_label"])
    Path(out_path).parent.mkdir(exist_ok=True)
    joblib.dump(pipe, out_path)
    return pipe

def load_intent_model(path="models/intent_model.joblib"):
    return joblib.load(path)
