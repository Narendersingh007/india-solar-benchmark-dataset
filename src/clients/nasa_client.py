from datetime import datetime

import requests

from clients.base_client import BaseWeatherClient
from models.download_models import DownloadResult
from utils.exceptions import DownloadError
from utils.logger import logger


class NASAClient(BaseWeatherClient):
    """
    Client responsible for communicating with NASA POWER API.
    """

    def __init__(
        self,
        session: requests.Session,
        api_config,
        pipeline_config,
    ):
        self._session = session
        self._api = api_config
        self._pipeline = pipeline_config

    def fetch_hourly_data(
        self,
        city,
        year_chunk,
    ) -> DownloadResult:

        params = self._build_parameters(city, year_chunk)

        response = self._make_request(params)

        self._validate_response(response)

        return self._create_result(
            city,
            year_chunk,
            response,
        )

    def _build_parameters(
        self,
        city,
        year_chunk,
    ):

        return {
            "start": year_chunk.start,
            "end": year_chunk.end,
            "latitude": city.latitude,
            "longitude": city.longitude,
            "community": self._api.community,
            "parameters": ",".join(self._pipeline.parameters),
            "format": self._api.format,
            "units": self._api.units,
            "time-standard": self._api.time_standard,
        }

    def _make_request(
        self,
        params,
    ):

        try:

            response = self._session.get(
                self._api.base_url,
                params=params,
                timeout=self._api.request_timeout,
            )

            return response

        except requests.RequestException as e:

            raise DownloadError(str(e))

    def _validate_response(
        self,
        response,
    ):

        if response.status_code != 200:

            raise DownloadError(
                f"NASA API returned {response.status_code}"
            )

    def _create_result(
        self,
        city,
        year_chunk,
        response,
    ) -> DownloadResult:

        return DownloadResult(
            city=city.name,
            latitude=city.latitude,
            longitude=city.longitude,
            start_date=year_chunk.start,
            end_date=year_chunk.end,
            content=response.content,
            downloaded_at=datetime.now(),
            content_length=len(response.content),
        )