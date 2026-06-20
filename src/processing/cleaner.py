import pandas as pd
class DataCleaner:
    def clean(
        self,
        df: pd.DataFrame,
    ):
        df = df.copy()
        df.columns = [
            c.strip()
            for c in df.columns
        ]
        df.drop_duplicates(
            inplace=True
        )
        df.replace(
            -999,
            pd.NA,
            inplace=True,
        )

        df.sort_values(
            "YYYYMMDDHH",
            inplace=True,
        )

        df.reset_index(
            drop=True,
            inplace=True,
        )
        return df