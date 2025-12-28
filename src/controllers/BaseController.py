import random
import string
from abc import ABC
from pathlib import Path

from helpers.config import get_settings


class BaseController(ABC):
    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = Path(__file__).parent.parent
        self.files_dir = self.base_dir / "assets" / "files"

    def generate_random_string(self, length: int = 12):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
