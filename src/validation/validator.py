from pathlib import Path
import pandas as pd
from utils.logger import logger

class DatasetValidator:
    def __init__(self):
        self.output_dir = Path(
            "data/metadata"
        )
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def validate(
        self,
        df: pd.DataFrame,
    ):
        report = {}
        report["rows"] = len(df)
        report["columns"] = len(df.columns)
        report["missing_values"] = (
            df.isna()
            .sum()
            .to_dict()
        )
        report["duplicates"] = (
            int(df.duplicated().sum())
        )

        report["memory_mb"] = round(
            df.memory_usage(
                deep=True
            ).sum()
            / 1024**2,
            2,
        )

        pd.DataFrame(
            report["missing_values"],
            index=["missing"]
        ).T.to_csv(
            self.output_dir
            / "missing_values.csv"
        )

        logger.info(
            "Dataset validation completed"
        )

        return report