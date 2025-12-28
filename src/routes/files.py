import logging

import aiofiles
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

from controllers import FileController
from helpers.config import Settings, get_settings
from models import ResoponseSignal

logger = logging.getLogger("uvicorn.error")

file_router = APIRouter(prefix="/api/v1/files", tags=["api_v1", "files"])


@file_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings),
) -> JSONResponse:
    file_controller = FileController()
    is_valid, result_signal = file_controller.validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"signal": result_signal}
        )

    unique_filepath = file_controller.generate_unique_filename(
        orig_file_name=file.filename, project_id=project_id
    )
    try:
        async with aiofiles.open(unique_filepath, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResoponseSignal.FILE_UPLOAD_FAILED.value},
        )

    return JSONResponse(content={"signal": ResoponseSignal.FILE_UPLOAD_SUCCESS.value})
