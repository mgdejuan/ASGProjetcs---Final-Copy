# inventory_app/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Flavor, Topping, Ingredient, Packaging, LogHistory

# Helper to map quantity to status string
def get_status_from_quantity(quantity):
    if quantity > 20: return "IN STOCK"
    if quantity > 5: return "LOW STOCK"
    if quantity > 0: return "CRITICAL"
    return "OUT OF STOCK"

# 1. Log Inventory Changes (Creation/Update/Restock)
@receiver(post_save, sender=Flavor)
@receiver(post_save, sender=Topping)
@receiver(post_save, sender=Ingredient) # Added
@receiver(post_save, sender=Packaging) # Added
def log_inventory_action(sender, instance, created, **kwargs):
    action = 'CREATED' if created else 'UPDATED'
    
    # NOTE: The 'staff' field is correctly left as None here.
    # The staff responsible will be logged accurately in the Restock VIEW.
    
    LogHistory.objects.create(
        staff=None, 
        action_taken=action,
        stock_status=get_status_from_quantity(instance.quantity),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk
    )

# 2. Log User Login
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    LogHistory.objects.create(
        staff=user,
        action_taken='LOGIN',
        stock_status=None, 
        # ContentType set to User model for logging non-inventory actions
        content_type=ContentType.objects.get(model='user'), 
        object_id=user.pk
    )