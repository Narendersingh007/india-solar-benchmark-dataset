from clients.nasa_client import NASAClient
from downloader.session import create_session
from services.downloader_service import DownloaderService
from storage.file_storage import FileStorage
from utils.config import config

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
    downloader.download_all()

if __name__ == "__main__":
    main()