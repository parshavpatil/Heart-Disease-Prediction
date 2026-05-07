from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model  = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Exactly 10 features matching your dataset
        features = [
            float(data["age"]),
            float(data["sex"]),
            float(data["cp"]),
            float(data["trestbps"]),
            float(data["chol"]),
            float(data["fbs"]),
            float(data["restecg"]),
            float(data["thalach"]),
            float(data["exang"]),
            float(data["oldpeak"]),
        ]

        scaled = scaler.transform([features])
        pred   = model.predict(scaled)[0]
        prob   = model.predict_proba(scaled)[0]

        return jsonify({
            "prediction" : int(pred),
            "result"     : "Disease Detected" if pred == 1 else "No Disease Detected",
            "prob_no"    : round(float(prob[0]) * 100, 2),
            "prob_yes"   : round(float(prob[1]) * 100, 2),
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
