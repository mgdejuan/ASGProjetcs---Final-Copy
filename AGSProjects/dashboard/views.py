from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Ingredient, Topping, Packaging
from decimal import Decimal # CRITICAL: All imports must be at the top.

# ------------------------------------------------------------------------------
# --- CORE VIEW ---
# ------------------------------------------------------------------------------
def dashboard(request): 
    # This must be defined for your home path.
    return render(request, 'sidebar/home.html') 

# ------------------------------------------------------------------------------
# --- FLAVORS CRUD ---
# ------------------------------------------------------------------------------
def flavors(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_str = request.POST.get('price')
        stock_str = request.POST.get('stock')

        if name and price_str and stock_str:
            try:
                price = Decimal(price_str)
                stock = int(stock_str)
                Flavor.objects.create(name=name, price=price, stock=stock) 
            except ValueError:
                print("Error: Invalid price or stock input for Flavor creation.")
                pass 
        return redirect('flavors')

    flavors = Flavor.objects.all()
    return render(request, 'dashboard/flavors.html', {'flavors': flavors})


def update_flavor(request, id):
    flavor = get_object_or_404(Flavor, id=id)
    if request.method == 'POST':
        flavor.name = request.POST.get('name')
        price_str = request.POST.get('price')
        stock_str = request.POST.get('stock')
        
        try:
            flavor.price = Decimal(price_str)
            flavor.stock = int(stock_str)
            flavor.save()
        except ValueError:
            print("Error: Invalid input for Flavor update.")
            pass
            
        return redirect('flavors')
    return render(request, 'dashboard/update_flavor.html', {'flavor': flavor})


def delete_flavor(request, id): # CONFIRMED FIX: This is the function Django was looking for earlier
    flavor = get_object_or_404(Flavor, id=id)
    flavor.delete()
    return redirect('flavors')

# ------------------------------------------------------------------------------
# --- INGREDIENTS CRUD ---
# ------------------------------------------------------------------------------
# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Ingredient, Topping, Packaging # Ensure all models are imported
from decimal import Decimal 

# --- Ingredients CRUD ---

def ingredients(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_str = request.POST.get('price')
        quantity_str = request.POST.get('quantity')

        if name and quantity_str and price_str:
            try:
                price = Decimal(price_str)
                quantity = int(quantity_str)
                
                Ingredient.objects.create(
                    name=name, 
                    price=price,
                    quantity=quantity, 
                ) 
            except ValueError:
                print("Error: Invalid price or quantity input for Ingredient creation.")
                # You might want to add Django messages here for user feedback
                pass
        return redirect('ingredients') # Always redirect back to the list after POST

    ingredients = Ingredient.objects.all()
    # Note: request.GET is passed implicitly and used by the template for in-place editing.
    return render(request, 'dashboard/ingredients.html', {'ingredients': ingredients})


def update_ingredient(request, id):
    # This view only receives the POST request from the in-place edit form.
    ingredient = get_object_or_404(Ingredient, id=id)

    if request.method == 'POST':
        ingredient.name = request.POST.get('name')
        price_str = request.POST.get('price')
        quantity_str = request.POST.get('quantity')
        
        try:
            ingredient.price = Decimal(price_str)
            ingredient.quantity = int(quantity_str)
            ingredient.save()
        except ValueError:
            print("Error: Invalid input for Ingredient update.")
            pass
            
        # CRITICAL: Redirect back to the main list page after saving
        return redirect('ingredients') 

    # If someone tries to navigate to this URL directly with GET, redirect them to the list.
    return redirect('ingredients') 


def delete_ingredient(request, id): 
    ingredient = get_object_or_404(Ingredient, id=id)
    ingredient.delete()
    return redirect('ingredients')

# ... include your other necessary views (dashboard, flavors, toppings, packaging) here ...
# ------------------------------------------------------------------------------
# --- TOPPINGS CRUD ---
# ------------------------------------------------------------------------------
def toppings(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_str = request.POST.get('price')
        stock_str = request.POST.get('stock')

        if name and price_str and stock_str:
            try:
                price = Decimal(price_str)
                stock = int(stock_str) 
                Topping.objects.create(name=name, price=price, stock=stock)
            except ValueError:
                print("Error: Invalid input for Topping creation.")
                pass
        return redirect('toppings')

    toppings = Topping.objects.all()
    return render(request, 'dashboard/toppings.html', {'toppings': toppings})


def update_topping(request, id):
    topping = get_object_or_404(Topping, id=id)
    if request.method == 'POST':
        topping.name = request.POST.get('name')
        price_str = request.POST.get('price')
        stock_str = request.POST.get('stock')
        
        try:
            topping.price = Decimal(price_str)
            topping.stock = int(stock_str)
            topping.save()
        except ValueError:
            print("Error: Invalid input for Topping update.")
            pass
            
        return redirect('toppings')
    return render(request, 'dashboard/update_topping.html', {'topping': topping})


def delete_topping(request, id):
    topping = get_object_or_404(Topping, id=id)
    topping.delete()
    return redirect('toppings')

# ------------------------------------------------------------------------------
# --- PACKAGING CRUD ---
# ------------------------------------------------------------------------------
def packaging(request):
    if request.method == 'POST':
        type_name = request.POST.get('type')
        cost_str = request.POST.get('cost')
        quantity_str = request.POST.get('quantity')

        if type_name and cost_str and quantity_str:
            try:
                cost = Decimal(cost_str) 
                quantity = int(quantity_str) 
                Packaging.objects.create(type=type_name, cost=cost, quantity=quantity)
            except ValueError:
                print("Error: Invalid input for Packaging creation.")
                pass
        return redirect('packaging')

    packaging_list = Packaging.objects.all()
    return render(request, 'dashboard/packaging.html', {'packaging_list': packaging_list})


def update_packaging(request, id):
    packaging = get_object_or_404(Packaging, id=id)
    if request.method == 'POST':
        packaging.type = request.POST.get('type')
        cost_str = request.POST.get('cost')
        quantity_str = request.POST.get('quantity')
        
        try:
            packaging.cost = Decimal(cost_str)
            packaging.quantity = int(quantity_str)
            packaging.save()
        except ValueError:
            print("Error: Invalid input for Packaging update.")
            pass
            
        return redirect('packaging')
    return render(request, 'dashboard/update_packaging.html', {'packaging': packaging})


def delete_packaging(request, id):
    packaging = get_object_or_404(Packaging, id=id)
    packaging.delete()
    return redirect('packaging')