from fastapi import FastAPI
from app.db import database


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def lolkek():
    return {'mes': 'kek'}
