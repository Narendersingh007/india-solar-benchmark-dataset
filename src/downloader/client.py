from datetime import datetime
import requests
from downloader.session import create_session
from models.download_models import DownloadResult
from utils.config import config
from utils.exceptions import DownloadError
from utils.logger import logger

class NASAClient :
    """Client responsible for communicating with NASA POWER API"""
    def __init__(self):
        self.session = create_session()
        self.api = config.api
        self.pipeline = config.pipeline

    def fetch_hourly_data(self,city,year_chunk):
        """ 
        Public API.
        Downloads hourly data and returns DownloadResult
        """
        params = self.build_parameters(city,year_chunk)
        response = self._make_request(params)
        self._validate_response(response)
        return self._create_result(
            city,
            year_chunk,
            response
        )
    
    def _build_parameters(self,city,year_chunk):
        """
        Pure function 
        
        No logging 
        NO HTTP
        No side effects
        """
        return {
            "start" : year_chunk.start,
            "end" : year_chunk.end,
            "latitude" : city.latitude,
            "longitude" : city.longitude,
            "community":self.api.community,
            "parameters": ",".join(self.pipeline.parameters),
            "format":self.api.format,
            "units":self.api.units,
            "time-standard":self.api.time_standard
        }
    
    def _make_request(self,params):
        """
        Boundary function
        Responsible for network Communication
        """
        logger.info("Sending request to NASA POWER API")

        try : 
            response = self.session.get(
                self.api_base_url,
                params=params,
                timeout= self.api.request_timeout,
            )
            return response
        except requests.exceptions.Timeout as exc :
            raise DownloadError(
                "NASA API request timed out."
            ) from exc
        except requests.exceptions.ConnectionError as exc :
            raise DownloadError(
                "Unable to connect to NASA POWER API."
            ) from exc

        except requests.exceptions.RequestException as exc :
            raise DownloadError(
                "Unexpected request error."
            ) from exc
    def _validate_response(self,response):
        """ 
        Validates HTTP Response 
        """
        if response.status_code != 200:
            raise DownloadError(
                f"NASA API returned status "
                f"{response.status_code}"
            )
        if not response.content:
            raise DownloadError(
                "NASA API returned empty content."
            )
    def _create_result(self,city,year_chunk,response):
        """
        Pure transformation
        """
        return DownloadResult(
            city=city.name,
            start_date=year_chunk.start,
            end_date=year_chunk.end,
            content=response.content,
            downloaded_at=datetime.now(),
            content_length=len(response.content),
        )