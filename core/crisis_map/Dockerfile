FROM python:3.12-slim
WORKDIR /app
COPY ../../requirements.txt ../../requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt
COPY backend ./backend
COPY frontend ./frontend
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
