from fastapi import FastAPI
from middleware.cors_middleware import setup_cors
from core.config import get_settings
from core.database import Base, engine

app = FastAPI(
    title="HireBOT Backend",
    description="FastAPI backend for HireBOT - Member 1 Environment & Security Setup",
    version="1.0.0"
)
from core.tasks import test_task

@app.get("/run-task")
def run_task():
    result = test_task.delay()
    return {"task_id": result.id, "status": "Task sent to Celery"}


# Enable CORS
setup_cors(app)

# Initialize database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    settings = get_settings()
    return {
        "message": "HireBOT Backend is running successfully!",
        "app_url": settings.APP_URL
    }
