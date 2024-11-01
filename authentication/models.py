from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# import argon2
from utils.models import TrackObjectStateMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin, TrackObjectStateMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    USER_ID_FIELD = "uuid"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# class Otp(TrackObjectStateMixin):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     otp = models.CharField(unique=True, blank=False)
#     expiry_date = models.DateTimeField(default=)
#     is_used = models.BooleanField(default=False)
#     expired = models.BooleanField(default=False)

#     def hash_otp(self, value: int):
#         salt = CustomUser.objects.get()
