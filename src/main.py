from clients.nasa_client import NASAClient
from downloader.session import create_session
from services.downloader_service import DownloaderService
from storage.file_storage import FileStorage
from utils.config import config
from pipeline.dataset_pipeline import DatasetPipeline

def main():
    session = create_session()
    client = NASAClient(
        session=session,
        api_config=config.api,
        pipeline_config=config.pipeline,
    )
    storage = FileStorage()
    downloader = DownloaderService(
        client=client,
        storage=storage,
    )
    pipeline = DatasetPipeline()
    downloader.download_all()
    pipeline.run()

if __name__ == "__main__":
    main()