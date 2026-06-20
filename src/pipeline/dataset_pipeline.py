from processing.merger import CSVMerger
from processing.cleaner import DataCleaner
from features.feature_engineer import FeatureEngineer
from validation.validator import DatasetValidator
from metadata.metadata_generator import MetadataGenerator

from utils.logger import logger


class DatasetPipeline:

    def __init__(self):
        self.merger = CSVMerger()
        self.cleaner = DataCleaner()
        self.feature_engineer = FeatureEngineer()
        self.validator = DatasetValidator()
        self.metadata = MetadataGenerator()
    def run(self):
        logger.info("Starting dataset pipeline")
        df = self.merger.merge_all()
        df = self.cleaner.clean(df)
        df = self.feature_engineer.transform(df)
        self.validator.validate(df)
        self.metadata.generate(df)
        logger.info("Dataset pipeline completed")
        return df