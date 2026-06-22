from pathlib import Path
import pandas as pd

from utils.config import config
from utils.logger import logger


class MetadataGenerator:

    def __init__(self):
        self.output_dir = Path("data/metadata")

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(self, df: pd.DataFrame):

        schema = pd.DataFrame({
            "column": df.columns,
            "dtype": [str(dtype) for dtype in df.dtypes]
        })

        schema.to_csv(
            self.output_dir / "schema.csv",
            index=False,
        )

        stats = df.describe(include="all")
        stats.to_csv(
            self.output_dir / "statistics.csv"
        )

    def generate_city_metadata(self):

        rows = []

        for city in config.cities:
            rows.append(
                {
                    "CITY": city.name,
                    "LATITUDE": city.latitude,
                    "LONGITUDE": city.longitude,
                }
            )

        city_df = pd.DataFrame(rows)

        city_df.to_csv(
            self.output_dir / "city_metadata.csv",
            index=False,
        )

        logger.info(
            "Generated city metadata"
        )

        return city_df