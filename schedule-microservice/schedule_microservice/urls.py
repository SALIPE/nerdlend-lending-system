from django.urls import path
from schedule_app import views

urlpatterns = [
    path('schedules/', views.ScheduleListView.as_view(), name='schedule-list-create'),
    path('schedules/by-id/<int:pk>/', views.FindScheduleView.as_view(), name='schedule-by-id'),
    path('schedules/return/<int:pk>/', views.ReturnView.as_view(), name='schedule-withdraw')
]