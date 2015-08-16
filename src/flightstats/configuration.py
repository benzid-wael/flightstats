# -*- coding: utf-8 -*-


class Configuration(object):
    """
    Class responsible for configuration of your FlightStats account.
    """

    base_uri = "https://api.flightstats.com/flex"

    @staticmethod
    def configure(app_id, app_key, use_http_errors=True):
        Configuration.app_id = app_id
        Configuration.app_key = app_key
        Configuration.use_http_errors = use_http_errors

    @staticmethod
    def instantiate():
        return Configuration(
            app_id=Configuration.app_id,
            app_key=Configuration.api_key,
            use_http_errors=Configuration.use_http_errors
        )

    @staticmethod
    def api_version():
        return "1"

    def __init__(self, app_id, api_key, use_http_errors=True):
        self.app_id = app_id
        self.api_key = api_key
        self.use_http_errors = use_http_errors
        self.protocol = "rest"
        self.format = "json"
        self.version = "v1"
