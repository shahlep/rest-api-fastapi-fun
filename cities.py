from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

db = []


class City(BaseModel):
    name: str
    timezone: str


@app.get('/')
def index():
    return {'key': 'value'}
