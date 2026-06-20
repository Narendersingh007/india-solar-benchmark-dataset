from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen = True,slots = True)
class DownloadResult :
    """
    Immutable model representing one successfull download
    """
    city: str
    latitude: float
    longitude: float
    start_date: int
    end_date: int
    content: bytes
    downloaded_at: datetime
    content_length: int