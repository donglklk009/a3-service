import uvicorn
from entity.request import HandReq, SpeedReq
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import hand_model, robot_model

app = FastAPI()

host: str = "0.0.0.0"
port: int = 8080

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Test"}

@app.post("/speed")
def change_speed(req: SpeedReq):
    return hand_model.change_speed(req)


@app.post("/hand")
def hand(req: HandReq):
    return hand_model.process(req)


@app.post("/voice")
def voice():
    return {"Hello": "World"}


if __name__ == "__main__":
    #robot_model.forward()
    #robot_model.reverse()
    #robot_model.turn_left()
    #robot_model.turn_right()
    uvicorn.run("app.main:app", loop="asyncio", host=host, port=port, workers=10)

