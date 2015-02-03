from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "esp_2015"

    def ready(self):
        import_module("esp_2015.receivers")
