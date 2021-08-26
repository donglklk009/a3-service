from pydantic import BaseModel


class HandReq(BaseModel):
    id_dev: int
    direction: int
    speed: int
