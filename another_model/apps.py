from django.apps import AppConfig


class AnotherModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'another_model'
