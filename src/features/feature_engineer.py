import numpy as np
import pandas as pd

class FeatureEngineer:
    def __init__(self):
        self.city = CityEnricher()
        self.cyclic = CyclicFeatureGenerator()
        self.lag = LagFeatureGenerator()
        self.rolling = RollingFeatureGenerator()
        
    def transform(
        self,
        df: pd.DataFrame,
    ):
        df = df.copy()
        dt = pd.to_datetime(
            df["YYYYMMDDHH"],
            format="%Y%m%d%H",
        )
        df["datetime"] = dt
        df["year"] = dt.dt.year
        df["month"] = dt.dt.month
        df["day"] = dt.dt.day
        df["hour"] = dt.dt.hour
        df["weekday"] = dt.dt.weekday
        df["week"] = dt.dt.isocalendar().week.astype(int)
        df["quarter"] = dt.dt.quarter
        df["is_weekend"] = (
            df["weekday"] >= 5
        ).astype(int)
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

        return df