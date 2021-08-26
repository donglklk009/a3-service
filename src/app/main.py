import uvicorn
from entity.request import HandReq
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import hand_model

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
    return {"Hello": "World"}


@app.post("/hand")
def hand(req: HandReq):
    return hand_model.process(req)


@app.post("/voice")
def voice():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=host, port=port, workers=10)
