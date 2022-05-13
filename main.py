from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Blog lists"}


@app.get('/blog/unpublished')
async def unpublished():
    return {'message': 'unpublished blogs'}


@app.get('/blog/{id}')
async def show(id: int):
    return {'message': id}
