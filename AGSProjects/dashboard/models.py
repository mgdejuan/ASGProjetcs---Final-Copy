from django.db import models

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# myapp/models.py 

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # 💥 CRITICAL FIX: Add the stock field back
    stock = models.PositiveIntegerField(default=0) 
    # ----------------------------------
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# In your models.py file:

# myapp/models.py 
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) 
    quantity = models.PositiveIntegerField(default=0)
    # The 'stock' field is removed from the model entirely.
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

# ... include your other models (Flavor, Topping, Packaging) here ...

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.stock} available)"


class Packaging(models.Model):
    type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} ({self.quantity} pcs)"
