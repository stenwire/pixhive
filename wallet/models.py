import uuid

from django.db import models

from utils.models import TrackObjectStateMixin

# Create your models here.


class Account(TrackObjectStateMixin):
    account_name = models.CharField()
    account_number = models.CharField()
    bank_code = models.CharField()
    bank_name = models.CharField()
    currency = models.CharField()
    acct_type = models.CharField(default="nuban")

    def __str__(self) -> str:
        return super().__str__()


class Wallet(TrackObjectStateMixin):
    balance = models.FloatField()
    dedicated_account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) -> str:
        return self.balance


class Transactions(TrackObjectStateMixin):
    by = models.ForeignKey("Collector")
    status = models.CharField(default="pending")
    transaction_reference = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True
    )

    def __str__(self) -> str:
        return self.transaction_reference
