from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from src.models import train_intent_model

df = pd.read_csv("data/rfqs.csv")
train, test = train_test_split(df, test_size=.2, random_state=42, stratify=df["intent_label"])
model = train_intent_model(train)
pred = model.predict(test["raw_rfq_text"])
print("Accuracy:", round(accuracy_score(test["intent_label"], pred),4))
print("Macro F1:", round(f1_score(test["intent_label"], pred, average="macro"),4))
print(classification_report(test["intent_label"], pred))
print("Confusion matrix:")
print(confusion_matrix(test["intent_label"], pred))
Path("models").mkdir(exist_ok=True)
pd.DataFrame({"actual":test["intent_label"],"predicted":pred}).to_csv("models/intent_predictions.csv",index=False)
