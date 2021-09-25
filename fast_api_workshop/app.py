"""
fast_api_workshop base module.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}
