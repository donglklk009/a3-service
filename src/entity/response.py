import typing

from pydantic import BaseModel


class Response(BaseModel):
    code: int
    message: str
    data: typing.Any
