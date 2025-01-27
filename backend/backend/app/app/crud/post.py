from typing import List, Optional
from app.models.post import PostDocument
from app.schemas.post_schema import PostCreate

class PostCRUD:
    @staticmethod
    async def create_post(post: PostCreate) -> PostDocument:
        post_doc = PostDocument(content=post.content)
        await post_doc.insert()
        return post_doc
    
    @staticmethod
    async def get_post() -> List[PostDocument]:
        posts = await PostDocument.find_all().sort("-created_at").to_list()
        return posts
    
    @staticmethod
    async def get_post(post_id: str) -> Optional[PostDocument]:
        post = await PostDocument.get(post_id)
        return post