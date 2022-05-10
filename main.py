from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to my library"}
# /list all books
# /book-by-index/
# /get-random-book
# /add-book
# /get-book?id=
