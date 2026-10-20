from fastapi import FastAPI
from app.database.database import Base, engine
from app.models import user, subject, tutor

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def hello():
    return {"Hello Worl"}