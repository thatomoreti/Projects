from fastapi import FastAPI
from Routers import users, posts, login
from models import Base
from db import engine

#Instantiate FastAPI program/app
app = FastAPI()

#Creating the db models
Base.metadata.create_all(bind=engine)

#Include all routers/ incorporate
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(login.router)


#Know when API is running
@app.get("/")
def root():
    return {"message": "API is up and  running!"}