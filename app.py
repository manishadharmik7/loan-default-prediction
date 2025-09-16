from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/loan_default_model.pkl")

# Save the exact feature order from training
TRAIN_FEATURES = [
    "Employed", "Bank Balance", "Annual Salary",
    "Balance_to_Salary", "Log_Salary", "Log_Balance"
]

@app.route("/")
def home():
    return "✅ Loan Default Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])

        # Recompute engineered features
        df["Balance_to_Salary"] = df["Bank Balance"] / (df["Annual Salary"] + 1)
        df["Log_Salary"] = np.log1p(df["Annual Salary"])
        df["Log_Balance"] = np.log1p(df["Bank Balance"])

        # Keep only features used in training (ignore extras)
        df = df.reindex(columns=TRAIN_FEATURES, fill_value=0)

        # Prediction
        proba = model.predict_proba(df)[:, 1][0]
        pred = int(proba > 0.5)

        return jsonify({
            "prediction": pred,
            "probability_default": float(proba)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
