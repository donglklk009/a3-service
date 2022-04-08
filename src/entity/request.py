from pydantic import BaseModel


class HandReq(BaseModel):
    direction: int
    speed: int
