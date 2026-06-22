from pathlib import Path
from utils.logger import logger
class DatasetSplitter:
    def split(self, df):

        train = df[df["year"] <= 2022]
        val = df[
            df["year"] == 2023
        ]

        test = df[
            df["year"] >= 2024
        ]

        output_dir = Path(
            "data/splits"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        train.to_parquet(
            output_dir / "train.parquet",
            index=False,
        )

        val.to_parquet(
            output_dir / "val.parquet",
            index=False,
        )

        test.to_parquet(
            output_dir / "test.parquet",
            index=False,
        )
        logger.info(
            f"Train: {train.shape}"
        )

        logger.info(
            f"Val: {val.shape}"
        )

        logger.info(
            f"Test: {test.shape}"
        )
        return train, val, test