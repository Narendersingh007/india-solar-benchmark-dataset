TARGET = "ALLSKY_SFC_SW_DWN"

class RollingFeatureGenerator:

    @staticmethod
    def transform(df):

        grouped = (
            df.groupby("CITY")[TARGET]
        )

        df["rolling_mean_24"] = (
            grouped.transform(
                lambda x: x.rolling(
                    24,
                    min_periods=1,
                ).mean()
            )
        )

        df["rolling_std_24"] = ((
            grouped.transform(
                    lambda x: x.rolling(
                        24,
                        min_periods=1,
                    ).std()
                ).fillna(0)
            )
        )

        df["rolling_mean_168"] = (
            grouped.transform(
                lambda x: x.rolling(
                    168,
                    min_periods=1,
                ).mean()
            )
        )
        df["rolling_max_24"] = (
            grouped.transform(
                lambda x: x.rolling(
                    24,
                    min_periods=1
                ).max()
            )
        )
        df["rolling_min_24"] = (
            grouped.transform(
                lambda x: x.rolling(
                    24,
                    min_periods=1
                ).min()
            )
        )

        return df