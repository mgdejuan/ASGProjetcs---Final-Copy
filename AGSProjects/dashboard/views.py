from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Ingredient, Topping, Packaging


# ----- FLAVORS CRUD -----
def flavors(request):
    flavors = Flavor.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Flavor.objects.create(name=name, price=price)
        return redirect('flavors')
    return render(request, 'dashboard/flavors.html')

def update_flavor(request, id):
    flavor = get_object_or_404(Flavor, id=id)
    if request.method == 'POST':
        flavor.name = request.POST.get('name')
        flavor.price = request.POST.get('price')
        flavor.save()
        return redirect('flavors')
    return render(request, 'dashboard/update_flavor.html', {'flavor': flavor})

def delete_flavor(request, id):
    flavor = get_object_or_404(Flavor, id=id)
    flavor.delete()
    return redirect('flavors')


# ----- INGREDIENTS CRUD -----
def ingredients(request):
    ingredients = Ingredient.objects.all()
    if request.method == 'POST':
        name = request.POST.get('ingredient')
        stock = request.POST.get('stock')
        Ingredient.objects.create(name=name, stock=stock)
        return redirect('ingredients')
    return render(request, 'dashboard/ingredients.html', {'ingredients': ingredients})

def update_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    if request.method == 'POST':
        ingredient.name = request.POST.get('ingredient')
        ingredient.stock = request.POST.get('stock')
        ingredient.save()
        return redirect('ingredients')
    return render(request, 'dashboard/update_ingredient.html', {'ingredient': ingredient})

def delete_ingredient(request, id):
    ingredient = get_object_or_404(Ingredient, id=id)
    ingredient.delete()
    return redirect('ingredients')


# ----- TOPPINGS CRUD -----
def toppings(request):
    toppings = Topping.objects.all()
    if request.method == 'POST':
        name = request.POST.get('topping')
        price = request.POST.get('price')
        Topping.objects.create(name=name, price=price)
        return redirect('toppings')
    return render(request, 'dashboard/toppings.html', {'toppings': toppings})

def update_topping(request, id):
    topping = get_object_or_404(Topping, id=id)
    if request.method == 'POST':
        topping.name = request.POST.get('topping')
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
    packaging_list = Packaging.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')
        cost = request.POST.get('cost')
        Packaging.objects.create(type=type, cost=cost)
        return redirect('packaging')
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
