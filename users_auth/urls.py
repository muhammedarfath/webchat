from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CheckUsernameView, LoginView, SignUpView





urlpatterns = [
    path('check_username/', CheckUsernameView.as_view(), name='check_username'),
    path("login/", LoginView.as_view(), name="login"),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

