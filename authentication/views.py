from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .utils import generate_otp, verify_otp, send_otp
from .serializers import UserModelSerializer, VerifyOTPSerializer, CustomTokenObtainPairSerializer

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
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VerifyOTPView(UpdateAPIView):
    """Generic View for verifying OTP and updating
        user verification status
    """

    queryset = CustomUser.objects.all()
    serializer_class = VerifyOTPSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # TODO: Extract user
        user = self.get_object()

        # TODO: Extract user OTP
        user_otp = user.email_otp
        email_otp = validated_data["otp"]

        if verify_otp(email_otp, user_otp):
            # TODO:
            # update user is_verified field to True
            user.is_verified = True
            # update user email_otp field to null
            user.email_otp = None
            user.save()
        else:
            # TODO: add return result
            return Response(
                {"detail": "Invalid OTP or OTP has expired."},
                status=status.HTTP_400_BAD_REQUEST
            )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer