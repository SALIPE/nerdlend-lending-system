"""
URL configuration for customer_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from customer_app import views
from django.urls import path

urlpatterns = [
    # Customer endpoints
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    
    # Customer Charge Log endpoints
    path('customers/customer-chargelogs/', views.CustomerChargeLogListView.as_view(), name='customer-charge-log-list'),
    path('customers/customer-chargelogs/<int:pk>/', views.CustomerChargeLogDetailView.as_view(), name='customer-charge-log-detail'),
    
    # Penalty endpoints
    path('customers/penalties/', views.PenaltyListView.as_view(), name='penalty-list'),
    path('customers/penalties/<int:pk>/', views.PenaltyDetailView.as_view(), name='penalty-detail'),
    
    # Balance
    path("customers/account/balance/", views.BalanceView.as_view(), name="account-balance"),
    path("customers/account/recharge/", views.RechargeBalanceView.as_view(), name="account-recharge"),
    
    path('customers/internal/by-id/<int:pk>/',views.CustomerInternalView.as_view(), name="internal-get")
]
