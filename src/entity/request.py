from pydantic import BaseModel

class SpeedReq(BaseModel):
    speed: int

class HandReq(BaseModel):
    direction: int
