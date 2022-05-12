from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

db = []


class City(BaseModel):
    name: str
    timezone: str


@app.get('/')
def index():
    return {"msg": "Hello World"}


@app.get('/cities')
def get_cities():
    return db


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id - 1)
    return {}
