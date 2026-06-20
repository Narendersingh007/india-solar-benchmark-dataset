class NASAClient(BaseWeatherClient):
    def __init__(
            self,
            session,
            api_config,
            pipeline_config,
    ):
        self._session = session
        self._api = api_config
        self._pipeline = pipeline_config