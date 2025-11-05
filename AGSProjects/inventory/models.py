# inventory_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# --- 1. Base Inventory Models (Add Ingredient and Packaging) ---

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model): # Added
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class Packaging(models.Model): # Added
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name
        
# --- 2. Central Log History Model ---

class LogHistory(models.Model):
    ACTION_CHOICES = [
        ('LOGIN', 'User Login'),
        ('RESTOCKED', 'Restocked'),
        ('CREATED', 'Created Product'),
        ('UPDATED', 'Updated Details'),
        ('DELETED', 'Deleted Product'),
    ]
    
    date_and_time = models.DateTimeField(auto_now_add=True)
    action_taken = models.CharField(max_length=20, choices=ACTION_CHOICES)
    stock_status = models.CharField(max_length=20, null=True, blank=True)
    staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    # Generic Foreign Key
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('content_type', 'object_id')

    @property
    def product_name(self):
        return self.product_object.name if self.product_object else "System"

    def __str__(self):
        return f"[{self.date_and_time.strftime('%m-%d-%y')}] {self.product_name} - {self.action_taken}"