from fastapi import APIRouter, HTTPException
from typing import List

from app.crud.post import PostCRUD
from app.schemas.post_schema import Post, PostCreate

router = APIRouter()

@router.post("/", response_model=Post)
async def create_post(post: PostCreate):
    return await PostCRUD.create_post(post)

@router.get("/", response_model=List[Post])
async def get_posts():
    return await PostCRUD.get_posts()

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: str):
    post = await PostCRUD.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
