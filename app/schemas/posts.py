from pydantic import BaseModel
from .user import UserOut

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostIn(PostBase): 
    pass


class PostOut(PostBase):
    id: int
    owner_id: int
    owner: UserOut

    # class config:
    #     orm_mode = True