from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome to my library"}


# /list all books
@app.get("/list-all-books")
async def list_all_books():
    return {"message": "List all books"}
# /book-by-index/
# /get-random-book
# /add-book
# /get-book?id=
