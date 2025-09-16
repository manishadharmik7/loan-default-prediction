# ===== Base Image =====
FROM python:3.11-slim

# ===== Set working directory =====
WORKDIR /app

# ===== Copy requirements first (for caching) =====
COPY requirements.txt .

# ===== Upgrade pip & install dependencies =====
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt --timeout 120 --retries 5

# ===== Copy all project files =====
COPY . .

# ===== Expose Streamlit default port =====
EXPOSE 8501

# ===== Command to run your app =====
#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
