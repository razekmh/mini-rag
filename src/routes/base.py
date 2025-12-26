from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])


@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    app_settings = get_settings()
    return {
        "message": f"Welcome to the {app_settings.APP_NAME} API! {app_settings.APP_VERSION}"
    }
