from processing.merger import CSVMerger
from processing.cleaner import DataCleaner
from features.feature_engineer import FeatureEngineer
from validation.validator import DatasetValidator
from metadata.metadata_generator import MetadataGenerator
from processing.dataset_splitter import DatasetSplitter
from pathlib import Path
from utils.logger import logger


class DatasetPipeline:

    def __init__(self):
        self.merger = CSVMerger()
        self.cleaner = DataCleaner()
        self.feature_engineer = FeatureEngineer()
        self.splitter = DatasetSplitter()
        self.validator = DatasetValidator()
        self.metadata = MetadataGenerator()
    def run(self):
        logger.info("Starting dataset pipeline")
        self.metadata.generate_city_metadata()
        df = self.merger.merge_all()
        df = self.cleaner.clean(df)
        df = self.feature_engineer.transform(df)
        self.validator.validate(df)
        self.splitter.split(df)
        ml_ready_dir = Path("data/ml_ready")
        ml_ready_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        df.to_parquet(
            ml_ready_dir / "india_multicity_ml_ready.parquet",
            index=False,
        )
        self.metadata.generate(df)
        logger.info("Dataset pipeline completed")
        return df