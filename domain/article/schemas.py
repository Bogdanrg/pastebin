from typing import Optional

from pydantic import BaseModel, model_validator

from domain.article.enums import VisibilityEnum


class ArticleModel(BaseModel):
    visibility: VisibilityEnum = VisibilityEnum.public
    content: str
    expiration: int = 86400
    secret: Optional[str] | None = None

    @model_validator(mode='after')
    def validate_secret_and_visibility(self):
        secret = self.secret
        visibility = self.visibility
        if visibility == 'private' and secret is None: raise ValueError("Private visibility requires a defined secret")
        if visibility == 'public' and secret is not None: raise ValueError("Public visibility doesn't require a secret")

        return self
