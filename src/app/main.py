import uvicorn
from entity.request import HandReq
from fastapi import FastAPI
from model import hand_model

app = FastAPI()

host: str = "0.0.0.0"
port: int = 8080


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/hand")
def hand(req: HandReq):
    return hand_model.process(req)


@app.post("/voice")
def voice():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=host, port=port, workers=10)
