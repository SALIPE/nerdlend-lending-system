"""
URL configuration for auth_microservice project.

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
    1. Import the include() function: from django.urls import include, pathusers
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from auth_app import views
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users', views.UserListView.as_view(), name='user-handles'),
    path('users/user-token', views.UserObtainTokenPairView.as_view(), name='user_token_obtain_pair'),
    path('users/user-token-refresh', views.UserRefreshTokenView.as_view(), name='user_token_refresh'),
    path('users/user-type', views.HandleUserType.as_view(), name='create_user_type'),
    ]
