from fastapi import FastAPI

app = FastAPI()


# minimal app - as suggested in https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/")
async def home():
    return {"message": "Welcome to my todo list"}

# Get --> Read Todo

# POST --> Create Todo
# PUT --> Update Todo
# DELETE --> Delete Todo

