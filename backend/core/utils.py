import uuid
from datetime import datetime

def generate_uuid() -> str:
    """Generate a unique UUID string."""
    return str(uuid.uuid4())

def get_current_timestamp() -> str:
    """Return the current UTC timestamp as ISO string."""
    return datetime.utcnow().isoformat()
