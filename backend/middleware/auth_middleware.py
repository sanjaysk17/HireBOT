from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from core.security import decode_token

auth_scheme = HTTPBearer()

async def verify_auth(request: Request):
    """Simple authentication middleware using JWT."""
    credentials = await auth_scheme(request)
    token = credentials.credentials
    payload = decode_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    request.state.user = payload
    return payload
