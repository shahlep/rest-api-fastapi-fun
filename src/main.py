from fastapi import FastAPI
import src.services as _services

app = FastAPI()

_services.create_database()

# https://fastapi.tiangolo.com/tutorial/sql-databases/



