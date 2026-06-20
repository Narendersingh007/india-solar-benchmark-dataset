
from datetime import datetime
import requests
from clients.base_client import BaseWeatherClient
from models.download_models import DownloadResult
from utils.exceptions import DownloadError
from utils.logger import logger
class NASAClient(BaseWeatherClient):
    def __init__(
            self,
            session,
            api_config,
            pipeline_config,
    ):
        self._session = session
        self._api = api_config
        self._pipeline = pipeline_config