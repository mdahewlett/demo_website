from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostCreate(BaseModel):
    content: str

class Post(BaseModel):
    id: str
    content: str
    created_at: datetime