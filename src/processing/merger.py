from pathlib import Path
import pandas as pd
from utils.config import config
from utils.logger import logger
class CSVMerger:
    def __init__(self):
        self.raw_dir = Path(
            config.pipeline.output_directory
        )
        self.processed_dir = Path(
            "data/processed"
        )
        self.processed_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def merge_city(self, city_name):
        files = sorted(
            self.raw_dir.glob(
                f"{city_name}_*.csv"
            )
        )
        dfs = [
            pd.read_csv(file, skiprows=10)
            for file in files
        ]
        merged = pd.concat(
            dfs,
            ignore_index=True,
        )

        output = (
            self.processed_dir
            / f"{city_name}.csv"
        )

        merged.to_csv(
            output,
            index=False,
        )

        logger.info(
            f"Merged {city_name}"
        )

        return merged

    def merge_all(self):
        all_frames = []
        for city in config.cities:
            df = self.merge_city(
                city.name
            )
            df["CITY"] = city.name
            all_frames.append(df)
        final = pd.concat(
            all_frames,
            ignore_index=True,
        )

        final.to_csv(
            self.processed_dir
            / "india_multicity.csv",
            index=False,
        )
        return final