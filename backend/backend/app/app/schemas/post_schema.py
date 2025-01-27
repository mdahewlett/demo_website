from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, handler):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict[str, Any]) -> dict[str, Any]:
        field_schema.update(type="string")
        return field_schema

class PostCreate(BaseModel):
    content: str

class Post(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    content: str
    created_at: datetime

    model_config = {
        "json_encoders": {ObjectId: str},
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }