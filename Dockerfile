FROM python:3.11-slim
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir fastapi uvicorn requests
EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]