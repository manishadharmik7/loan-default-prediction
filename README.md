# 🚀 Loan Default Prediction App

An end-to-end Machine Learning project for predicting loan defaults.
Built using **Python, Scikit-learn, XGBoost, Flask API, Streamlit UI, and Docker**.

🔗 **GitHub Repo:** [https://github.com/manishadharmik7/loan-default-prediction](https://github.com/manishadharmik7/loan-default-prediction)
🔗 **Live Flask API (Render):** [https://loan-default-prediction-5mm2.onrender.com/](https://loan-default-prediction-5mm2.onrender.com/) 

---

## 📂 Project Structure

```
loan-default-prediction/
│── data/                 # Dataset
│── notebooks/            # EDA + Model building
│── models/               # Saved ML models (.pkl / .json)
│── app.py                # Flask API
│── streamlit_app.py      # Streamlit UI
│── requirements.txt      # Dependencies
│── Dockerfile            # Docker setup
└── README.md             # Project guide
```

---

## ▶️ Running Locally

### **1️⃣ Start Flask API**

```bash
python app.py
```

Runs at:

```
http://127.0.0.1:5000
```

#### **Test API using curl**

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"bank_balance":100000,"annual_salary":500000,"employment_status":"Employed"}'
```

---

### **2️⃣ Start Streamlit UI**

```bash
streamlit run streamlit_app.py
```

Now open in browser 👉 [http://localhost:8501](http://localhost:8501)

---

## 🐳 Run with Docker

### **Build Image**

```bash
docker build -t loan-default-app .
```

### **Run Container**

```bash
docker run -p 5000:5000 loan-default-app
```

---

## ✅ What This Project Demonstrates

* End-to-end ML lifecycle
* EDA and data preprocessing
* Model training (Scikit-learn + XGBoost)
* Flask REST API deployment
* Streamlit frontend UI
* Docker containerization

---
