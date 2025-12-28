import aiofiles
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

from controllers import FileController, ProjectController
from helpers.config import Settings, get_settings

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
    file_path = project_dir_path / file.filename
    async with aiofiles.open(file_path, "wb") as f:  # type: ignore[unresolved-reference]
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    return {"signal": result_signal}
