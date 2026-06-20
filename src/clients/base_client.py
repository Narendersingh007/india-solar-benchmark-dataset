from abc import abstractmethod,ABC

from models.config_models import City, YearChunk
from models.download_models import DownloadResult

class BaseWeatherClient(ABC):
    """
    Abstract base class for all weather data providers.
    """
    @abstractmethod
    def fetch_hourly_data(self,city : City , year_chunk : YearChunk,)->DownloadResult:
        """Fetch hourly data from a weather provider."""

        raise NotImplementedError