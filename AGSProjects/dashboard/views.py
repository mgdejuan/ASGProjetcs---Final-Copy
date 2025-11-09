from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Ingredient, Topping, Packaging


def dashboard(request):
    return render(request, 'dashboard/home.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor

# Combined view for listing, adding, and updating flavors
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor

from django.shortcuts import render, get_object_or_404, redirect
from .models import Flavor

def flavors(request, id=None, delete_id=None):
    # Delete flavor if delete_id is provided
    if delete_id:
        flavor_to_delete = get_object_or_404(Flavor, id=delete_id)
        flavor_to_delete.delete()
        return redirect('flavors')

    # Add or Update flavor
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if id:  # Update existing
            flavor = get_object_or_404(Flavor, id=id)
            flavor.name = name
            flavor.price = price
            flavor.quantity = quantity
            flavor.save()
        else:  # Add new
            if name and price and quantity is not None:
                Flavor.objects.create(name=name, price=price, quantity=quantity)

        return redirect('flavors')

    # For GET request
    flavors = Flavor.objects.all()
    flavor_to_edit = get_object_or_404(Flavor, id=id) if id else None

    return render(request, 'dashboard/flavors.html', {
        'flavors': flavors,
        'flavor_to_edit': flavor_to_edit
    })


# ----- INGREDIENTS CRUD -----
def ingredients(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')

        if name and quantity:
            Ingredient.objects.create(name=name, quantity=quantity)
        return redirect('ingredients')

    ingredients = Ingredient.objects.all()
    return render(request, 'dashboard/ingredients.html', {'ingredients': ingredients})


def update_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    if request.method == 'POST':
        ingredient.name = request.POST.get('name')
        ingredient.quantity = request.POST.get('quantity')
        ingredient.save()
        return redirect('ingredients')
    return render(request, 'dashboard/update_ingredient.html', {'ingredient': ingredient})


def delete_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    ingredient.delete()
    return redirect('ingredients')


# ----- TOPPINGS CRUD -----
def toppings(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')

        if name and price:
            Topping.objects.create(name=name, price=price)
        return redirect('toppings')

    toppings = Topping.objects.all()
    return render(request, 'dashboard/toppings.html', {'toppings': toppings})


def update_topping(request, id):
    topping = get_object_or_404(Topping, id=id)
    if request.method == 'POST':
        topping.name = request.POST.get('name')
        topping.price = request.POST.get('price')
        topping.save()
        return redirect('toppings')
    return render(request, 'dashboard/update_topping.html', {'topping': topping})


def delete_topping(request, id):
    topping = get_object_or_404(Topping, id=id)
    topping.delete()
    return redirect('toppings')


# ----- PACKAGING CRUD -----
def packaging(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        cost = request.POST.get('cost')

        if type and cost:
            Packaging.objects.create(type=type, cost=cost)
        return redirect('packaging')

    packaging_list = Packaging.objects.all()
    return render(request, 'dashboard/packaging.html', {'packaging_list': packaging_list})


def update_packaging(request, id):
    packaging = get_object_or_404(Packaging, id=id)
    if request.method == 'POST':
        packaging.type = request.POST.get('type')
        packaging.cost = request.POST.get('cost')
        packaging.save()
        return redirect('packaging')
    return render(request, 'dashboard/update_packaging.html', {'packaging': packaging})


def delete_packaging(request, id):
    packaging = get_object_or_404(Packaging, id=id)
    packaging.delete()
    return redirect('packaging')
