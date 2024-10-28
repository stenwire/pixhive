import pyotp
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import config.settings as settings

totp = pyotp.TOTP(pyotp.random_base32(), interval=300)  # 5 minutes validity


def generate_otp():
    return totp.now()


def verify_otp(otp, user_otp):
    return totp.verify(otp) and otp == user_otp


def send_otp(receiver, otp):
    subject = "OTP for Pixhive email verification"
    html_message = render_to_string("mail_template.html", {"otp": otp})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = receiver
    send_mail(
        subject, plain_message, from_email, [to], html_message=html_message
    )
