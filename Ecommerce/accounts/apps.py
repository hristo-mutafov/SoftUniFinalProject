from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecommerce.accounts'

    def ready(self):
        import Ecommerce.accounts.signals
