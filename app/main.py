from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.endpoints import (
    user,
    post,
    auth
)
from pydantic_settings import BaseSettings
import uvicorn

# posts.Base.metadata.create_all(bind=engine)
# users.Base.metadata.create_all(bind=engine)
# vote.Base.metadata.create_all(bind=engine)

origins = [
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, prefix="/posts", tags=["Post"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router)
@app.get("/")
def index():
    return "this is first page get request"


