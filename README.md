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


---

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
🏷 Resume Keywords
End-to-End ML · EDA · Feature Engineering · Flask API · Streamlit · Docker · MLOps Basics

✅ This repo demonstrates the full ML lifecycle:
EDA → Model Training → Deployment → API + UI → Dockerization


### 4. GitHub push (ready-to-copy commands)

# Initialize repo
git init
git add .
git commit -m "Initial commit - Loan Default Prediction App"

# Add remote (replace with your repo link)
git remote add origin https://github.com/manishadharmik7/loan-default-prediction.git

# Push code
git branch -M main
git push -u origin main