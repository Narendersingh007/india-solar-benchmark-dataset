TARGET = "ALLSKY_SFC_SW_DWN"


class LagFeatureGenerator:

    @staticmethod
    def transform(df):
        grouped = df.groupby("CITY")[TARGET]
        df["lag_1"] = grouped.shift(1)
        df["lag_3"] = grouped.shift(3)
        df["lag_6"] = grouped.shift(6)
        df["lag_12"] = grouped.shift(12)
        df["lag_24"] = grouped.shift(24)
        df["lag_168"] = grouped.shift(168)
        return df