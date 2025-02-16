import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
df = pd.read_csv("news_dataset.csv")

# Drop missing values
df.dropna(inplace=True)

# Features (text) and Labels (fake=1, real=0)
X = df["text"]
y = df["label"]

# Vectorize text data
vectorizer = TfidfVectorizer(max_features=5000)
X_transformed = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save Model & Vectorizer
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model Trained and Saved as 'fake_news_model.pkl'!")
