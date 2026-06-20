from pathlib import Path
from models.download_models import DownloadResult
from utils.config import config
from utils.logger import logger

class FileStorage :
    """
    Responsible for persisting downloaded files.
    """
    def __init__(self):
        self.output_dir = Path(config.pipeline.output_directory)
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def build_filename(
        self,
        city: str,
        start_date: int,
        end_date: int,
    ) -> str:
        return f"{city}_{start_date}_{end_date}.csv"
    
    def save(
        self,
        result: DownloadResult,
    ) -> Path:

        filename = self.build_filename(
            result.city,
            result.start_date,
            result.end_date,
        )

        file_path = self.output_dir / filename

        file_path.write_bytes(
            result.content
        )

        logger.info(
            f"Saved {filename}"
        )

        return file_path

    def exists(
        self,
        city: str,
        start_date: int,
        end_date: int,
    ) -> bool:

        filename = self.build_filename(
            city,
            start_date,
            end_date,
        )

        return (self.output_dir / filename).exists()

    def list_files(self):
        return sorted(
            self.output_dir.glob("*.csv")
        )

    def read(
        self,
        filename: str,
    ) -> bytes:
        return (
            self.output_dir / filename
        ).read_bytes()