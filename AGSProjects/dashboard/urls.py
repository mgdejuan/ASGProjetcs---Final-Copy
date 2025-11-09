from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Flavors
    path('flavors/', views.flavors, name='flavors'),  # add / list
    path('flavors/<int:id>/', views.flavors, name='update_flavor'),  # edit inline
    path('flavors/delete/<int:delete_id>/', views.flavors, name='delete_flavor'),  # delete inline


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
