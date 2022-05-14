from fastapi import FastAPI
import services as _services

app = FastAPI()

_services.create_database()

