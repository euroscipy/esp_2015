from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "esp_2015.proposals"
    label = "esp_2015.proposals"

