from fastapi import APIRouter, UploadFile, Depends
from helpers.config import get_settings, Settings
from controllers import FileController

file_router = APIRouter(prefix="/api/v1/files", tags=["api_v1", "files"])


@file_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings),
) -> bool:
    is_valid = FileController().validate_uploaded_file(file=file)
    return is_valid
