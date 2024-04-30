"""Serve API routes."""
from fastapi import FastAPI
import helpers

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
