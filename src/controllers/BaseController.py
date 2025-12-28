from abc import ABC
from helpers.config import get_settings


class BaseController(ABC):
    def __init__(self):
        self.app_settings = get_settings()
