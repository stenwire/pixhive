from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserModelSerializer,
    VerifyOTPSerializer,
)
from .utils import generate_otp, send_otp


class UserCreateView(CreateAPIView):
    """Generic View for Listing and Creating User Profiles"""

    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = CustomUser.objects.create_user(**validated_data)
        # TODO: add email otp sending
        # Generate and save OTPs
        email_otp = generate_otp()
        user.email_otp = email_otp
        print("user.email_otp 1: ", user.email_otp)
        user.save()
        print("user.email_otp 2: ", user.email_otp)
        user_email = user.email
        send_otp(user_email, email_otp)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class VerifyOTPView(GenericAPIView):
    """Generic View for verifying OTP and updating
    user verification status
    """

    serializer_class = VerifyOTPSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=request.user,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
