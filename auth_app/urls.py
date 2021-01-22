from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import CustomTokenRefreshView
from .views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_token'),
    path('/refresh', CustomTokenRefreshView.as_view(), name='auth_token_refresh'),
    path('/register', RegisterView.as_view(), name='auth_register')
]
