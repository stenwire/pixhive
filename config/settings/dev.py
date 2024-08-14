from datetime import timedelta

from .base import *  # noqa 403
import os

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] = timedelta(days=30)  # noqa 405

# class EmailConfig(BaseSettings):
#     EMAIL_BACKEND: str
#     EMAIL_HOST: str  # Use your email provider's SMTP server
#     EMAIL_PORT: int
#     EMAIL_USE_TLS: bool = True
#     EMAIL_HOST_USER: str
#     EMAIL_HOST_PASSWORD: str

# EMAIl_CONFIG = EmailConfig()
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='stephenchiboy760@gmail.com'
EMAIL_HOST_PASSWORD='rmacdqimebbqvity'