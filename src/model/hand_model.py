from entity.request import HandReq
from entity.response import Response
from . import robot_model

TS = 0.2 # seconds
def process(req: HandReq) -> Response:
    print("Hello")
    if req.direction == 1:
        robot_model.turn_left(TS) 
    elif req.direction == 2:
        robot_model.turn_right(TS) 
    elif req.direction == 3:
        robot_model.forward(TS) 
    elif req.direction == 4:
        robot_model.reverse(TS) 
    return Response(
        code=0,
        message="OK",
        data=req
    )