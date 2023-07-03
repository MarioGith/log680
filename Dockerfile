# Stage 1: Build Stage
FROM python:3.9 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Runtime Stage
FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /app .

CMD ["python", "main.py"]