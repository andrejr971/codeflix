from django.apps import AppConfig


class CategoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # update name to match the app name
    name = 'src.django_project.category_app'
