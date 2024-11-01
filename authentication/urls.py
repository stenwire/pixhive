from django.urls import path
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

from .views import CustomTokenObtainPairView, UserCreateView, VerifyOTPView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path(
        "login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("otp-verify/", VerifyOTPView.as_view(), name="otp_verification"),
]
