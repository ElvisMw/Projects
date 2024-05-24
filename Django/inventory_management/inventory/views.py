from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, Product, Inventory
from .forms import SupplierForm, ProductForm, InventoryForm


def index(request):
    """
    Renders the home page.
    """
    return render(request, 'inventory/index.html')

def home(request):
    """
    Renders the home page and displays all inventory items.
    """
    inventory_items = Inventory.objects.all()
    return render(request, 'inventory/index.html', {'inventory_items': inventory_items})


def supplier_list(request):
    """
    Renders the supplier list page and displays all suppliers.
    """
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})


def product_list(request):
    """
    Renders the product list page and displays all products.
    """
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def inventory_list(request):
    """
    Renders the inventory list page and displays all inventory items.
    """
    inventory_items = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items})


def create_product(request):
    """
    Renders the product form page and creates a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})


def create_inventory(request):
    """
    Renders the inventory form page and creates a new inventory item.
    """
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})


def update_inventory(request, pk):
    """
    Renders the inventory form page and updates an existing inventory item.
    """
    inventory_item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory_item)
    return render(request, 'inventory/inventory_form.html', {'form': form})


def delete_inventory(request, pk):
    """
    Renders the confirmation page to delete an inventory item.
    """
    inventory_item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'inventory_item': inventory_item})


def update_product(request, pk):
    """
    Renders the product form page and updates an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})


def delete_product(request, pk):
    """
    Renders the confirmation page to delete a product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

