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
            self.raw_dir.glob(f"{city_name}_*.csv")
        )
        dfs = []
        for file in files:
            header_line = self.find_header_line(file)
            df = pd.read_csv(
                file,
                skiprows=header_line,
                na_values=[-999, -999.0],
                low_memory=False,
            )
            dfs.append(df)
        merged = pd.concat(
            dfs,
            ignore_index=True,
        )
        output = (
            self.processed_dir / f"{city_name}.csv"
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
            df = self.merge_city(city.name)
            df["CITY"] = city.name
            all_frames.append(df)

        final = pd.concat(
            all_frames,
            ignore_index=True,
        )

        final["datetime"] = pd.to_datetime(
            dict(
                year=final["YEAR"],
                month=final["MO"],
                day=final["DY"],
                hour=final["HR"],
            )

        )
        final.sort_values(
            ["CITY", "datetime"],
            inplace=True,

        )
        final.to_csv(
            self.processed_dir / "india_multicity.csv",
            index=False,

        )

        final.to_parquet(
            self.processed_dir / "india_multicity.parquet",
            index=False,

        )

        logger.info(
            "Merged complete India multicity dataset"
        )

        return final
    @staticmethod
    def find_header_line(file_path: Path) -> int:
        """
        Find the row containing the NASA CSV header.
        """
        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as f:

            for index, line in enumerate(f):
                if line.startswith("YEAR,"):
                    return index

        raise ValueError(
            f"CSV header not found: {file_path}"
        )