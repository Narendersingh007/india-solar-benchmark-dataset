import numpy as np
import pandas as pd
from features.city_enricher import CityEnricher
from features.cyclic_features import CyclicFeatureGenerator
from features.physics_features import PhysicsFeatureGenerator
from features.lag_features import LagFeatureGenerator
from features.rolling_features import RollingFeatureGenerator
from features.solar_features import  SolarFeatureGenerator

class FeatureEngineer:
    def __init__(self):
        self.city = CityEnricher()
        self.cyclic = CyclicFeatureGenerator()
        self.physics = PhysicsFeatureGenerator()
        self.lag = LagFeatureGenerator()
        self.rolling = RollingFeatureGenerator()
        self.solar = SolarFeatureGenerator()
    def transform(
        self,
        df: pd.DataFrame,
    ):
        df = df.copy()
        if "datetime" in df.columns:
            dt = pd.to_datetime(df["datetime"])
        else:
            dt = pd.to_datetime(
                dict(
                    year=df["YEAR"],
                    month=df["MO"],
                    day=df["DY"],
                    hour=df["HR"],
                )
            )
        df["dayofyear"] = dt.dt.dayofyear
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
        df = self.city.transform(df)
        df = self.solar.transform(df)
        df = self.cyclic.transform(df)
        df = self.physics.transform(df)
        df = df.sort_values(["CITY", "datetime"]).reset_index(drop=True)
        df = self.lag.transform(df)
        df = self.rolling.transform(df)

        return df