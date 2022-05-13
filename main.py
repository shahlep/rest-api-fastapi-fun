from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# query params
@app.get('/blog')
async def home(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'message': f'{limit} published blog from Blog lists!'}
    else:
        return {'message': 'No published blog available'}


@app.get('/blog/unpublished')
async def unpublished():
    return {'message': 'unpublished blogs'}


@app.get('/blog/{id}')
async def show(id: int):
    return {'message': id}


@app.get('/blog/{id}/comments')
async def show(id: int, limit: int = 5):
    return {'message': f'Blogger {id} got {limit} comments'}
