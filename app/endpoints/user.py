
from fastapi import Depends, HTTPException, APIRouter
from app.models.users import User
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import hash_password
from app.schemas.user import UserIn, UserOut

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user:UserIn ,
                db:Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    user.password = hashed_pwd
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=UserOut)
def get_user_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found with the given id ")
    return user
    

