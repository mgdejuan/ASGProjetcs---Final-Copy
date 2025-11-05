# inventory_app/apps.py
from django.apps import AppConfig

class InventoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory_app'

    def ready(self):
        # Import signals to ensure they connect when Django starts
        import inventory.signals