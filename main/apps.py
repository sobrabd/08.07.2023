from django.apps import AppConfig
from django.core.signals import setting_changed, request_finished


def my_callback(sender, **kwargs):
    print("Setting changed!")


class MainDEVConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class MainPRODConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        print("i am ready")
        request_finished.connect(my_callback)
