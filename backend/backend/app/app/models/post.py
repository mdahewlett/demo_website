from datetime import datetime
from typing import Optional
from beanie import Document
from pydantic import Field

class PostDocument(Document):
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "posts"