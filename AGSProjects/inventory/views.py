# inventory_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q # Used for efficient querying, if needed
from .models import Flavor, Topping, Ingredient, Packaging, LogHistory
from django.contrib.contenttypes.models import ContentType

# Helper function (duplicate of the signal helper for view consistency)
def get_status_from_quantity(quantity):
    if quantity > 20: return "IN STOCK"
    if quantity > 5: return "LOW STOCK"
    if quantity > 0: return "CRITICAL"
    return "OUT OF STOCK"

# Helper to aggregate all inventory data
def aggregate_inventory_data():
    inventory_list = []
    
    # Define models and their categories
    models_to_include = [
        (Flavor, 'Flavors'), 
        (Topping, 'Toppings'), 
        (Ingredient, 'Ingredients'), 
        (Packaging, 'Packaging'),
    ]

    for Model, category in models_to_include:
        for item in Model.objects.all():
            inventory_list.append({
                'id': item.pk,
                'name': item.name,
                'category': category,
                'quantity': item.quantity,
                'status': get_status_from_quantity(item.quantity),
                'last_updated': item.last_updated.strftime('%Y-%m-%d') # Format date for HTML
            })
    return inventory_list

@login_required
def dashboard_view(request):
    # Retrieve the 10 most recent logs for the Dashboard table
    recent_logs = LogHistory.objects.order_by('-date_and_time')[:10]
    
    context = {
        'recent_logs': recent_logs,
        'user_name': request.user.username,
        # ... other dashboard components
    }
    return render(request, 'home.html', context) 

@login_required
def inventory_view(request):
    # Data aggregation for "Manage Product Stocks" table
    full_inventory = aggregate_inventory_data() 
    
    context = {
        'inventory_items': full_inventory,
    }
    return render(request, 'inventory.html', context)

@login_required
def restock_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_category = request.POST.get('item_category')
        quantity_to_add = int(request.POST.get('quantity_added', 0))
        
        # Determine the model based on category
        Model_Map = {'Flavors': Flavor, 'Toppings': Topping, 'Ingredients': Ingredient, 'Packaging': Packaging}
        Model = Model_Map.get(item_category)

        if not Model or not item_id or quantity_to_add <= 0:
            # Handle invalid submission (redirect with error message in a real app)
            return redirect('inventory_view') 

        item = get_object_or_404(Model, pk=item_id)
        
        # 1. Update stock
        old_quantity = item.quantity
        item.quantity += quantity_to_add
        item.save() # This triggers the automatic 'UPDATED' signal, which is fine

        # 2. Create the explicit, detailed 'RESTOCKED' log entry
        LogHistory.objects.create(
            staff=request.user, # **Correctly logs the staff member**
            action_taken='RESTOCKED',
            stock_status=get_status_from_quantity(item.quantity),
            details=f"Restocked by +{quantity_to_add} units. Qty changed from {old_quantity} to {item.quantity}.",
            content_type=ContentType.objects.get_for_model(Model),
            object_id=item.pk
        )
        # You could also delete the generic 'UPDATED' signal log created above if you only want the 'RESTOCKED' log.
        
        return redirect('inventory_view')
    
    return redirect('inventory_view')