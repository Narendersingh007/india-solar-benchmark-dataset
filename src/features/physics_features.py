import numpy as np 
import pandas as pd

class PhysicsFeatureGenerator:
    def transform(
        self,
        df: pd.DataFrame,
    ):
        df = df.copy()
        df["TEMP_HUMIDITY"] = (
            df["T2M"] * df["RH2M"]
        )
        df["DEWPOINT_SPREAD"] = (
            df["T2M"] - df["T2MDEW"]
        )
        df["WIND_POWER"] = (
            df["WS10M"] ** 3
        )
        df["PRESSURE_TEMP"] = (
            df["PS"] * df["T2M"]
        )
        df["CLEARNESS_TEMP"] = (
            df["ALLSKY_KT"] * df["T2M"])
        df["CLEARNESS_HUMIDITY"] = (
            df["ALLSKY_KT"] * df["RH2M"]
        )
        df["TEMP_WIND"] = (
            df["T2M"] * df["WS10M"]
        )
        return df