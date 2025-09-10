from flask import Flask, send_file, jsonify, request
import requests
import zipfile
import os
import io
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Use Agg backend for matplotlib headless rendering in Docker
plt.switch_backend('Agg')

app = Flask(__name__)

# Point logging through NGINX reverse proxy
LOGGING_URL = "http://nginx/logs"

@app.route("/analysis/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    # Save uploaded file
    zip_path = "uploaded.zip"
    file.save(zip_path)

    # Extract ZIP contents
    extract_dir = "data"
    os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    # Find first CSV file
    csv_file = None
    for root, _, files in os.walk(extract_dir):
        for f in files:
            if f.endswith(".csv"):
                csv_file = os.path.join(root, f)
                break
        if csv_file:
            break

    if csv_file is None:
        return jsonify({"error": "No CSV file found"}), 400

    # Read dataset
    df = pd.read_csv(csv_file)

    numeric_df = df.select_dtypes(include=['number'])
    # Create correlation heatmap figure
    plt.figure(figsize=(20, 20))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

    # Save image to bytes buffer
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format="png")
    img_bytes.seek(0)

    # Close the figure to free memory
    plt.close()

    # Log to logging-service via NGINX (non-blocking with timeout)
    try:
        requests.post(LOGGING_URL, json={
            "service": "analysis-service",
            "message": f"Analyzed dataset with shape {numeric_df.shape}"
        }, timeout=5)
    except Exception as e:
        print("Logging failed:", e)

    return send_file(img_bytes, mimetype="image/png")

if __name__ == "__main__":
    # Run on 0.0.0.0 so accessible within Docker network, port 5050 internally
    app.run(host="0.0.0.0", port=5050, debug=True)
