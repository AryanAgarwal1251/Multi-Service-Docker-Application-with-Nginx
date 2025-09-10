from flask import Flask, jsonify, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    score = analyzer.polarity_scores(text)
    sentiment = (
        "Positive" if score["compound"] > 0.05
        else "Negative" if score["compound"] < -0.05
        else "Neutral"
    )

    # Return valid JSON response
    return jsonify({"sentiment": sentiment, "scores": score})

if __name__ == "__main__":
    # Bind to 0.0.0.0 for Docker network access and run on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
