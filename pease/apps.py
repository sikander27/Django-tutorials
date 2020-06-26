from django.apps import AppConfig


class PeaseConfig(AppConfig):
    name = 'pease'

    def ready(self):
        import pease.signals
