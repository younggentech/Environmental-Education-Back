from typing import Optional
from pydantic import BaseModel, Field


class ProblemSchema(BaseModel):
    heading: str = Field(...)
    text: str = Field(...)
    img: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "heading": "Environmental issue",
                "text": "The most important issue is deforestration, this problem occures in modern areas.",
                "img": "/static/deforestration.jpg",
            }
        }


class UpdateProblemModel(BaseModel):
    heading: Optional[str]
    text: Optional[str]
    img: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "heading": "Environmental issue",
                "text": "The most important issue is deforestration, this problem occures in modern areas.",
                "img": "/static/deforestration.jpg",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data] if not isinstance(data, list) else data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}