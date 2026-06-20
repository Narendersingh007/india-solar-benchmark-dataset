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
            [-999, -999.0],
            pd.NA,
            inplace=True,
        )

        if "datetime" not in df.columns:

            df["datetime"] = pd.to_datetime(
                dict(
                    year=df["YEAR"],
                    month=df["MO"],
                    day=df["DY"],
                    hour=df["HR"],
                )
            )

        df.sort_values(
            ["CITY", "datetime"],
            inplace=True,
        )

        df.reset_index(
            drop=True,
            inplace=True,
        )

        return df