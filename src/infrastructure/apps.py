from django.apps import AppConfig


class InfrastructureConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "src.infrastructure"
    label = "infrastructure"  # Importante para referenciarla
