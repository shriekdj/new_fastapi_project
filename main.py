from fastapi import FastAPI, Optional
from pydantic import BaseModel

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None

posts = ["post1", "post2", "post3"]

app = FastAPI()

@app.get("/")
def get_root():
 return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
  return {"posts": posts}


