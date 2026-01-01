import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "tickets_dataset.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")

def train_models():
  if not os.path.exists(DATA_PATH):
      raise FileNotFoundError(f"CSV not found at {DATA_PATH}")
  
  df = pd.read_csv(DATA_PATH)

  category_pipeline = Pipeline([
      ('vectorizer', TfidfVectorizer(stop_words='english')),
      ('classifier', MultinomialNB())
  ])

  priority_pipeline = Pipeline([
      ('vectorizer', TfidfVectorizer(stop_words='english')),
      ('classifier', MultinomialNB())
  ])

  category_pipeline.fit(df['description'], df['category'])
  priority_pipeline.fit(df['description'], df['priority'])

  joblib.dump(category_pipeline, 'models/model_category.joblib')
  joblib.dump(priority_pipeline, 'models/model_priority.joblib')

if __name__ == "__main__":
    train_models()