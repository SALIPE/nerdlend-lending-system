from django.urls import path
from trigger_app import views

urlpatterns = [
    path('send-email', views.TriggerEmailView.as_view(), name='trigger-send-email'),
    
]

