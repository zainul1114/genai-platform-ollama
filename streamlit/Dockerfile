FROM python:3.10-slim
RUN pip install streamlit requests
WORKDIR /app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
