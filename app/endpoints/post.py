
from fastapi import HTTPException, APIRouter,Depends, status
from sqlalchemy.orm import Session
from app.models import posts
from app.database import get_db
from app.schemas.posts import PostIn, PostOut
from app.oauth2 import get_current_user


router =  APIRouter()

@router.post("/", response_model=PostOut)
def createpost(postInput: PostIn,
               db: Session=Depends(get_db) ,current_user:int= Depends(get_current_user)):
    print(postInput)
    post = posts.Post(owner_id=current_user.id, **postInput.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/", response_model=list[PostOut])
def get_all_post(
    db: Session = Depends(get_db) ,current_user:int= Depends(get_current_user)

):
    
    # all_post = db.query(posts.Post).all()
    # return all_post

    """only get the post of your own user id not for everyone 
    """
    user_id =  current_user.id
    all_post = db.query(posts.Post).filter(posts.Post.owner_id==user_id).all()
    return all_post



@router.get("/{id}", response_model=PostOut)
def get_by_id(
    id: int, db: Session = Depends(get_db) ,current_user:int= Depends(get_current_user)
):
    result =  db.query(posts.Post).filter(posts.Post.id==id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="not found the id with post ")
    return result


@router.delete("/{id}")
def delete_post(

    id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    post = db.query(posts.Post).filter(posts.Post.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no post found to delete with the given id")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="you are not the owner of the post to delete it ")
    db.delete(post)    
    # alternative of delete is post.delete()
    db.commit()
    return {"message":"post deleted"}