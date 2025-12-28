from fastapi import APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import FileController, ProjectController

file_router = APIRouter(prefix="/api/v1/files", tags=["api_v1", "files"])


@file_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings),
) -> dict:
    is_valid, result_signal = FileController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"signal": result_signal}
        )
    project_dir_path = ProjectController().get_project_path(project_id=project_id)

    return {"signal": result_signal}
