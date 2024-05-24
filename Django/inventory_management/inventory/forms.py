# inventory/forms.py
from django import forms
from .models import Supplier, Product, Inventory

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'supplier']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']
