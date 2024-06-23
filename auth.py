from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
import os

API_KEY_NAME = "api_key"
API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
