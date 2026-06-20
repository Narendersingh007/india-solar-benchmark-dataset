from pathlib import Path
import pandas as pd

class TimeSeriesSplitter:
    def __init__(self):
        self.output_dir = Path(
            "data/ml_ready"
        )
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def split(
        self,
        df: pd.DataFrame,
    ):
        train = df[
            df["year"] <= 2022
        ]
        validation = df[
            df["year"] == 2023
        ]
        test = df[
            df["year"] >= 2024
        ]
        train.to_csv(
            self.output_dir / "train.csv",
            index=False,
        )
        validation.to_csv(
            self.output_dir / "validation.csv",
            index=False,
        )
        test.to_csv(
            self.output_dir / "test.csv",
            index=False,
        )

        return train, validation, test