from ninja import Schema


class CustomUserInput(Schema):
    email: str
    password: str


class OTPInput(Schema):
    otp: int
