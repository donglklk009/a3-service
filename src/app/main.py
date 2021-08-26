import uvicorn
from fastapi import FastAPI

app = FastAPI()

host: str = "0.0.0.0"
port: int = 8080


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=host, port=port, workers=10)
