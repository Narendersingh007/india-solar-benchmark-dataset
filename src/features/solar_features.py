import pandas as pd
import pvlib
class SolarFeatureGenerator:

    def transform(
        self,
        df: pd.DataFrame,
    ):
        df = df.copy()
        results = []
        for city, city_df in df.groupby("CITY"):

            lat = city_df["LATITUDE"].iloc[0]
            lon = city_df["LONGITUDE"].iloc[0]

            times = pd.DatetimeIndex(pd.to_datetime(
                city_df["datetime"]
            )).tz_localize("Asia/Kolkata")

            location = pvlib.location.Location(
                latitude=lat,
                longitude=lon,
            )

            solar_position = (
                location.get_solarposition(
                    times
                )
            )

            clearsky = (
                location.get_clearsky(
                    times
                )
            )

            city_df["SOLAR_ZENITH"] = (
                solar_position["zenith"]
                .values
            )

            city_df["SOLAR_ELEVATION"] = (
                solar_position["elevation"]
                .values
            )

            city_df["SOLAR_AZIMUTH"] = (
                solar_position["azimuth"]
                .values
            )

            city_df["CLEARSKY_GHI"] = (
                clearsky["ghi"]
                .values
            )

            city_df["CLEARSKY_DNI"] = (
                clearsky["dni"]
                .values
            )

            city_df["CLEARSKY_DHI"] = (
                clearsky["dhi"]
                .values
            )
            city_df["AIR_MASS"] = (
                location.get_airmass(
                    solar_position=solar_position
                )["airmass_relative"]
            )

            results.append(city_df)
        return pd.concat(
            results,
            ignore_index=True,
        )