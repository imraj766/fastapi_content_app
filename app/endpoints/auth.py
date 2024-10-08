from fastapi import Depends, status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserLogIn
from app.models.users import User
from app import utils
from app.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm



router = APIRouter(tags=["authentication"])


@router.post("/login")
def login(user_cred: OAuth2PasswordRequestForm = Depends(),
    db: Session =  Depends(get_db)):
    user = db.query(User).filter(User.email==user_cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    if not utils.verify_password(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email or password")
    access_token = create_access_token(data={"user_id":user.id})
    return {"access_token":access_token, "token_type":"bearer"}
    



