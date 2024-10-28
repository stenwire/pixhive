from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.exceptions import InvalidOTP

from .models import CustomUser
from .schema import CustomUserInput
from .utils import verify_otp

# from utils.serializers import BaseSerializer


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data: CustomUserInput):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        """Overriding to remove Password Field when returning Data"""
        ret = super().to_representation(instance)
        ret.pop("password", None)
        return ret


class VerifyOTPSerializer(serializers.Serializer):
    email_otp = serializers.CharField(
        max_length=6, min_length=6, required=True
    )

    class Meta:
        model = CustomUser
        fields = ["email_otp"]

    def validate_email_otp(self, value):
        user = self.context["request"].user
        e_otp = user.email_otp
        print("email_otp: ", value)
        print("e_otp: ", e_otp)

        if not verify_otp(value, e_otp):
            raise InvalidOTP

        return e_otp

    @transaction.atomic
    def save(self):
        user = self.context["request"].user
        user.is_verified = True
        user.email_otp = None
        user.save()
        # self.validated_data["otp"].delete()
        return


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        credentials = {
            "email": attrs.get("email"),
            "password": attrs.get("password"),
        }

        user = authenticate(**credentials)

        if user:
            if not user.is_active:
                raise exceptions.AuthenticationFailed("User is deactivated")

            data = {}
            refresh = self.get_token(user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data
        else:
            raise exceptions.AuthenticationFailed(
                "No active account found with the given credentials"
            )
