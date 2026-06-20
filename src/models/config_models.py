from dataclasses import dataclass

@dataclass(frozen=True,slots = True)
class APIConfig :
    base_url : str 
    community : str 
    format : str 
    units : str 
    time_standard : str 
    request_timeout : str 
    retry_attempts : int 
    retry_delay : int

@dataclass
class City :
    name : str 
    latitude : float 
    longitude : float

@dataclass
class YearChunk:
    start: int
    end: int

@dataclass
class PipelineConfig:
    years: list[YearChunk]
    parameters: list[str]
    output_directory: str
    sleep_between_requests: int

@dataclass
class AppConfig :
    api : APIConfig
    pipeline : PipelineConfig
    cities : list[City]