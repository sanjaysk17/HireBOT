# 🐍 Backend Dockerfile

# 1️⃣ Use official Python image
FROM python:3.10-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy all files from backend folder
COPY . .

# 4️⃣ Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expose backend port
EXPOSE 8000

# 6️⃣ Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
