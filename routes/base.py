from fastapi import APIRouter, FastAPI

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])


@base_router.get("/")
def welcome():
    return {"message": "Welcome to the mini-rag API!"}
