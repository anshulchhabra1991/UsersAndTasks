import jwt
from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from jwt import PyJWTError
from datetime import datetime

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        authorization: str = request.headers.get('Authorization')
        if not authorization or not authorization.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization header missing or invalid"}
            )

        token = authorization.split(" ")[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token")

            exp = payload.get("exp")
            if exp and datetime.utcnow().timestamp() > exp:
                raise HTTPException(status_code=401, detail="Token expired")

            request.state.user = username

        except PyJWTError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid JWT token"}
            )

        response = await call_next(request)
        return response
