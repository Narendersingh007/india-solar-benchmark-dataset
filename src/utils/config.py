from pathlib import Path
import yaml
from models.config_models import (
    APIConfig,
    City,
    YearChunk,
    PipelineConfig,
    AppConfig,
)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "configs"

class ConfigLoader :
    @staticmethod
    def load_yaml(filename : str):
        file_path = CONFIG_DIR / filename
        with open(file_path, "r") as file :
            return yaml.safe_load(file)
    @classmethod
    def load(cls):
        api_dict = cls.load_yaml("api.yaml")
        cities_dict = cls.load_yaml("cities.yaml")
        pipeline_dict = cls.load_yaml("pipeline.yaml")
        api = APIConfig(**api_dict)
        cities = [
            City(**city)
            for city in cities_dict["cities"]
        ]
        years = [
            YearChunk(**year)
            for year in pipeline_dict["years"]
        ]
        pipeline = PipelineConfig(
            years=years,
            parameters=pipeline_dict["parameters"],
            output_directory=pipeline_dict["output_directory"],
            sleep_between_requests=pipeline_dict["sleep_between_requests"]
        )
        return AppConfig(
            api = api,
            pipeline=pipeline,
            cities=cities
        )
config = ConfigLoader.load()