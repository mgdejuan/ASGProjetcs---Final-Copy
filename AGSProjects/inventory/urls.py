# inventory_project/urls.py (Project-level)
from django.urls import path, include

urlpatterns = [
    # ... other paths
    path('', include('inventory_app.urls')),
]

# inventory_app/urls.py (App-level)
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dashboard_view, name='home'),
    path('inventory/', views.inventory_view, name='inventory_view'),
    # Use a generic name for the restock action
    path('inventory/restock/', views.restock_item, name='restock_item'), 
]