import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from data.loader import DatasetLoader

def train_models():
  loader = DatasetLoader()
  df = loader.load()

  category_pipeline = Pipeline([
      ('vectorizer', TfidfVectorizer()),
      ('classifier', MultinomialNB())
  ])

  priority_pipeline = Pipeline([
      ('vectorizer', TfidfVectorizer()),
      ('classifier', MultinomialNB())
  ])

  category_pipeline.fit(df['description'], df['category'])
  priority_pipeline.fit(df['description'], df['priority'])

  os.makedirs("models", exist_ok=True)

  joblib.dump(category_pipeline, 'models/model_category.joblib')
  joblib.dump(priority_pipeline, 'models/model_priority.joblib')

if __name__ == "__main__":
    train_models()