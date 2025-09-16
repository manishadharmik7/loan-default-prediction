## 🚀 Loan Default Prediction App

An end-to-end ML project for predicting loan defaults.  
Built with **Python, Scikit-learn, XGBoost, Flask API, Streamlit UI, and Docker**.

---

### 📂 Project Structure
loan-default-prediction/
│── data/ # Dataset
│── notebooks/ # EDA + Model building
│── models/ # Saved model (.pkl / .json)
│── app.py # Flask API
│── streamlit_app.py # Streamlit UI
│── requirements.txt # Dependencies
│── Dockerfile # Docker setup
│── README.md # Project guide


### ▶️ Running Locally

#### 1️⃣ Flask API

# Start Flask API
python app.py
# Runs at http://127.0.0.1:5000
# Test with:
curl -X POST http://127.0.0.1:5000/predict 
-H "Content-Type: application/json" -d '{"bank_balance":100000,"annual_salary":500000,"employment_status":"Employed"}'

# Start Streamlit UI
streamlit run streamlit_app.py
Now open 👉 http://localhost:8501

🐳 Run with Docker

# Build image
docker build -t loan-default-app .

# Run container
docker run -p 5000:5000 loan-default-app

✅ This repo demonstrates the full ML lifecycle:
EDA → Model Training → Deployment → API + UI → Dockerization

