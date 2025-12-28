from abc import ABC
from helpers.config import get_settings
from pathlib import Path


class BaseController(ABC):
    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = Path(__file__)
        self.files_dir = self.base_dir / "assets" / "files"
