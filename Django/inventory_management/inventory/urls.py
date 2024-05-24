# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='product_create'),
    path('products/<int:pk>/update/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/create/', views.create_inventory, name='create_inventory'),
    path('inventory/<int:pk>/edit/', views.update_inventory, name='update_inventory'),
    path('inventory/<int:pk>/delete/', views.delete_inventory, name='delete_inventory'),
]
