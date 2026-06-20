import pandas as pd

class CityEnricher:
    def __init__(self):
        self.metadata = pd.read_csv(
            "data/metadata/city_metadata.csv"
        )

    def transform(self, df):
        return df.merge(
            self.metadata,
            on="CITY",
            how="left",
        )