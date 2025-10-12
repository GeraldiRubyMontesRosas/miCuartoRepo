import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}


@app.get("/familia")
def get_familia():
    rows = ["Ruby", "Fabian", "Dulce"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Batman", "Superman", "Flash"]
    return rows