from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    description: str


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


# dynamic path with default query params
@app.get('/blog/{id}/comments')
async def show(id: int, limit: int = 5):
    return {'message': f'Blogger {id} got {limit} comments'}


@app.post('/blog')
async def create_post(blog: Blog):
    return {f'{blog.title} has been created with {blog.description}'}
