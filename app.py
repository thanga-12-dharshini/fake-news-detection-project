##main python file 
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model & vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        news_text = [data["text"]]

        # Convert text to vector
        text_vector = vectorizer.transform(news_text)

        # Predict
        prediction = model.predict(text_vector)[0]
        result = "Fake" if prediction == 1 else "Real"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message

if __name__ == '__main__':
    app.run(debug=True)
