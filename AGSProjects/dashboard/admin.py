# dashboard/admin.py

from django.contrib import admin
from .models import Flavor, Ingredient, Topping, Packaging

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_available', 'created_at')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    # FIX: Uses 'stock' to match the now-corrected model
    list_display = ('name', 'stock', 'is_available', 'created_at') 
    search_fields = ('name',)
    list_filter = ('is_available', 'created_at')


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_available', 'created_at')


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    # Note: Uses 'quantity' to match the Packaging model's field name
    list_display = ('type', 'cost', 'quantity', 'is_available', 'created_at') 
    search_fields = ('type',)
    list_filter = ('is_available', 'created_at')