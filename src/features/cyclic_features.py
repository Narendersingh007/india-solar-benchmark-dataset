import numpy as np
class CyclicFeatureGenerator:
    @staticmethod
    def transform(df):
        df["hour_sin"] = np.sin(
            2 * np.pi * df["hour"] / 24
        )
        df["hour_cos"] = np.cos(
            2 * np.pi * df["hour"] / 24
        )
        df["month_sin"] = np.sin(
            2 * np.pi * df["month"] / 12
        )
        df["month_cos"] = np.cos(
            2 * np.pi * df["month"] / 12
        )
        df["dayofyear_sin"] = np.sin(
            2 * np.pi * df["dayofyear"] / 365
        )
        df["dayofyear_cos"] = np.cos(
            2 * np.pi * df["dayofyear"] / 365
        )
        return df