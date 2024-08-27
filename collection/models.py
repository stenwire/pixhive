from django.db import models
from django.conf import settings
from utils.models import TrackObjectStateMixin
from accounts.models import Hiver, Collector

class Collection(TrackObjectStateMixin):
    owner = models.ForeignKey(
        Hiver,
        on_delete=models.CASCADE,
        related_name='collections'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pass_code = models.CharField(blank=True, null=True, unique=True)
    is_public = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    price = models.FloatField(blank=True, null=True)
    is_purchased = models.BooleanField(default=False)
    purchased_by = models.ForeignKey(
        Collector,
        on_delete=models.SET_NULL,
        related_name='collections',
        blank=True,
        null=True
    )
    collection_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PurchasedCollection(TrackObjectStateMixin):
    collector = models.ForeignKey(
        Collector,
        on_delete=models.SET_NULL,
        related_name='purchased_collection',
        blank=True,
        null=True
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        related_name='purchased_collection',
        blank=True,
        null=True
    )
    purchase_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.FloatField()

    def __str__(self):
        return f"{self.collector.user.email} purchased {self.collection.name} on {self.purchase_date}"