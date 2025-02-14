from django.contrib import admin
from django.urls import path
from product_app import views

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='products-handles'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/allproducts/', views.AllProductNoAuthView.as_view(), name='all-products'),

    
    path('products/favorites/', views.FavoriteView.as_view(), name='favorite-list'),
    path('products/favorites/<int:pk>/', views.TbfavoriteDetailView.as_view(), name='favorite-detail'),
    
    path('products/internal/validate-ids/', views.InternalValidateIdsView.as_view(), name='internal-validate-product-list'),
    path('products/internal/id-list/', views.InternalListView.as_view(), name='internal-product-list'),
    path('products/internal/update-storage/', views.InternalUpdateStorageView.as_view(), name='internal-update-storage'),
    path('products/internal/withdraw-storage/', views.InternalWitdrawStorageView.as_view(), name='internal-withdraw-storage'),
]
