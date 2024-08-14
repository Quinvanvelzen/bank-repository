from fastapi import FastAPI

from components import message

app = FastAPI()


@app.get("/")
def root() -> dict():
    return {"message": message.hello_world()}
