from celery import Celery

# Define the Celery app
celery_app = Celery(
    "hirebot",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def test_task():
    return "Celery is running successfully!"
