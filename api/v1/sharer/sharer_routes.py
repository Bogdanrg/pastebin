from boto3 import resource
from fastapi import APIRouter, Depends

from core.s3.services import get_s3_resource
from domain.article.schemas import ArticleModel
from services.article_service import ArticleService

sharer_router = APIRouter(prefix="/sharer")


@sharer_router.post("/article")
async def create_article(
    article: ArticleModel, s3_resource: resource = Depends(get_s3_resource)
) -> dict:
    response: str = await ArticleService.upload_article(
        s3_resource, article.content, article.expiration
    )
    return {"status": 200, "url": response}
