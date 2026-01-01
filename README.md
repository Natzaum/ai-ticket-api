# AI Ticket API

A REST API that validates and analyzes support ticket descriptions, automatically classifying them into predefined categories (billing, technical, account...) and estimating their priority level (low, medium, or high) using artificial intelligence.

## Tools and Technologies

### Backend/API
- **Python 3.12**
- **FastAPI**
- **Uvicorn**

### AI / Machine Learning
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Multinomial Naive Bayes**
- **Pandas**
- **Joblib**

### Dev & Ops Tools
- **Git + GitHub**
- **Pydantic**

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
### 2. Train the Model
Before running the API, generate the AI models:
```bash
python scripts/train.py
```
### 3. Start the API
```
cd app
uvicorn main:app --reload
```

Use postman or http://127.0.0.1:8000/docs
