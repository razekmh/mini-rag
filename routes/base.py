from fastapi import APIRouter, FastAPI

base_router = APIRouter()


@base_router.get("/")
def welcome():
    return {"message": "Welcome to the mini-rag API!"}
