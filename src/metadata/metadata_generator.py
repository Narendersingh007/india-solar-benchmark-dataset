from pathlib import Path
import pandas as pd

class MetadataGenerator:
    def __init__(self):
        self.output_dir = Path(
            "data/metadata"
        )
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        df: pd.DataFrame,

    ):
        schema = pd.DataFrame({
            "column": df.columns,
            "dtype": [
                str(dtype)
                for dtype in df.dtypes
            ]

        })

        schema.to_csv(
            self.output_dir
            / "schema.csv",
            index=False,
        )
        stats = df.describe(
            include="all"
        )
        stats.to_csv(
            self.output_dir
            / "statistics.csv"
        )