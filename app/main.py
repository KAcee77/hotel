from fastapi import FastAPI
from .db import get_session    

app = FastAPI()


@app.get("/")
async def lolkek():
    return {'mes': 'kek'}
