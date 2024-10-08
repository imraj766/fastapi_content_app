

from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from app.schemas.user import TokenBase
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data:dict):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


def veirfy_access_token(token, credential_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credential_exceptions
        token_data = TokenBase(id=id)
    except JWTError:
        raise credential_exceptions
    return token_data
    

def get_current_user(token: str = Depends(oauth2_scheme)):

    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="unauthorized")
    return veirfy_access_token(token, credential_exception)
