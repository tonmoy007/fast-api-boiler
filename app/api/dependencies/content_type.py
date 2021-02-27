from fastapi import Header, HTTPException

from app.resources import messages


async def check(content_type: str = Header(...)):
    if content_type != "application/json":
        raise HTTPException(status_code=401, detail=messages.INVALID_CONTENT_TYPE)
