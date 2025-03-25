from django.apps import AppConfig


class ExpensesConfig(AppConfig):  # Change from HelloWorldConfig to ExpensesConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expenses'


# this connects signals to the app
class ExpensesConfig(AppConfig):
    name = 'expenses'

    def ready(self):
        import expenses.signals  
