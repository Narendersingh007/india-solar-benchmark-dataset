from time import sleep
from tqdm import tqdm
from clients.nasa_client import NASAClient
from storage.file_storage import FileStorage
from utils.config import config
from utils.logger import logger


class DownloaderService:

    """
    Orchestrates downloading and storage.
    """
    def __init__(
        self,
        client: NASAClient,
        storage: FileStorage,
    ):
        self.client = client
        self.storage = storage

    def download_all(self):
        total = (
            len(config.cities)
            * len(config.pipeline.years)
        )
        logger.info(
            f"Starting download of {total} files"
        )
        progress = tqdm(
            total=total,
            desc="Downloading"
        )
        downloaded = 0
        skipped = 0
        failed = 0
        for city in config.cities:
            for year in config.pipeline.years:
                try:
                    if self.storage.exists(
                        city.name,
                        year.start,
                        year.end,
                    ):
                        skipped += 1
                        progress.update(1)
                        continue
                    result = (
                        self.client.fetch_hourly_data(
                            city,
                            year,
                        )
                    )
                    self.storage.save(
                        result
                    )
                    downloaded += 1
                    sleep(
                        config.pipeline.sleep_between_requests
                    )
                except Exception as e:
                    failed += 1
                    logger.error(
                        f"{city.name} "
                        f"{year.start}-{year.end} "
                        f"{str(e)}"
                    )
                progress.update(1)
        progress.close()
        logger.info(
            f"""
Download Summary
Downloaded : {downloaded}
Skipped    : {skipped}
Failed     : {failed}
"""
        )