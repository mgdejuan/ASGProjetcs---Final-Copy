from django.urls import path
from . import views

urlpatterns = [
    # Flavors
    path('flavors/', views.flavors, name='flavors'),
    path('flavors/update/<int:id>/', views.update_flavor, name='update_flavor'),
    path('flavors/delete/<int:id>/', views.delete_flavor, name='delete_flavor'),

    # Ingredients
    path('ingredients/', views.ingredients, name='ingredients'),
    path('ingredients/update/<int:id>/', views.update_ingredient, name='update_ingredient'),
    path('ingredients/delete/<int:id>/', views.delete_ingredient, name='delete_ingredient'),

    # Toppings
    path('toppings/', views.toppings, name='toppings'),
    path('toppings/update/<int:id>/', views.update_topping, name='update_topping'),
    path('toppings/delete/<int:id>/', views.delete_topping, name='delete_topping'),

    # Packaging
    path('packaging/', views.packaging, name='packaging'),
    path('packaging/update/<int:id>/', views.update_packaging, name='update_packaging'),
    path('packaging/delete/<int:id>/', views.delete_packaging, name='delete_packaging'),
]
