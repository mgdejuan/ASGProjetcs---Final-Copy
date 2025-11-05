from django.apps import AppConfig

class InventoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self):
        # Import signals to ensure they connect when Django starts
        import inventory.signals