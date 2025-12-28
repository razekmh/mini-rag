import re

from fastapi import UploadFile

from models import ResoponseSignal

from .BaseController import BaseController
from .ProjectController import ProjectController


class FileController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    def validate_uploaded_file(self, file: UploadFile) -> tuple[bool, str]:
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResoponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResoponseSignal.FILE_SIZE_EXCEEDED.value
        return True, ResoponseSignal.FILE_UPLOAD_SUCCESS.value

    def generate_unique_filename(
        self, orig_file_name: str | None, project_id: str
    ) -> str:
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)

        new_file_path = project_path / (random_key + "_" + cleaned_file_name)

        while new_file_path.is_file():
            random_key = self.generate_random_string()
            new_file_path = project_path / (random_key + "_" + cleaned_file_name)

        return new_file_path

    def get_clean_file_name(self, orig_file_name: str | None) -> str | None:
        if not orig_file_name:
            return None

        cleaned_file_name = re.sub(r"[ˆ\w.]", "", orig_file_name.strip())

        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
