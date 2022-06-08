from entity.request import HandReq, SpeedReq
from entity.response import Response
from . import robot_model
from sensor import distance

#TS = 0.2 # seconds
def process(req: HandReq) -> Response:
    print("process direction")
    curDis = distance('cm')
    if curDis <= 10: #if current distance less than 10cm
        robot_model.reverse()
    if req.direction == 1:
        robot_model.forward()
    elif req.direction == 2:
        robot_model.reverse() 
    elif req.direction == 3:
        robot_model.turn_left()
    elif req.direction == 4:
        robot_model.turn_right()
    elif req.direction == 5:
        robot_model.stop()
    elif req.direction == 6:
        robot_model.camera_turnleft()
    elif req.direction == 7:
        robot_model.camera_turnright()
    elif req.direction == 8:
        robot_model.camera_straight()
    return Response(
        code=0,
        message="OK",
        data=req
    )

def change_speed(req: SpeedReq):
    print("procees speed")
    if(req.speed < 0 or req.speed > 100):
        return Response(code=-1, message="speed = [0,100]", data=req)
    robot_model.change_speed(req.speed)
    return Response(
        code=0,
        message="OK",
        data=req
    )

