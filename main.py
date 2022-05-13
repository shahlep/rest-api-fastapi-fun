from fastapi import FastAPI

app = FastAPI()


# query params
@app.get('/blog')
async def home(limit):
    return {'message': f'{limit} blog from Blog lists!'}


@app.get('/blog/unpublished')
async def unpublished():
    return {'message': 'unpublished blogs'}


@app.get('/blog/{id}')
async def show(id: int):
    return {'message': id}
