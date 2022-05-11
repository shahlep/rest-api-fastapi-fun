import http

from fastapi import FastAPI

app = FastAPI()

todos = [
    {
        'id': '1',
        'activity': 'getting fresh'
    },
    {
        'id': '2',
        'activity': 'make breakfast'
    }
]


# minimal app - as suggested in https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/")
async def home():
    return {"message": "Welcome to my todo list"}


# Get --> Read Todo
@app.get('/todo', tags=['todos'], status_code=http.HTTPStatus.OK)
async def get_todos():
    return {'todos': todos}


# POST --> Create Todo
@app.post('/todo', tags=['todos'], status_code=http.HTTPStatus.CREATED)
async def create_todos(todo: dict):
    todos.append(todo)
    return {'data': 'New Item has been added'}
# PUT --> Update Todo
# DELETE --> Delete Todo
