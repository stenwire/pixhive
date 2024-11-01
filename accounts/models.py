from django.conf import settings
from django.db import models

from utils.models import TrackObjectStateMixin

# Create your models here.


class Hiver(TrackObjectStateMixin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hiver",
    )
    instagram = models.URLField(
        verbose_name="instagram", blank=True, null=True
    )
    twitter = models.URLField(verbose_name="twitter", blank=True, null=True)

    def __str__(self):
        return self.user.email


class Collector(TrackObjectStateMixin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collector",
    )
    # email = models.EmailField(verbose_name='collector_email', unique=True)
    # collection_id = models.ForeignKey(
    # "Collection", on_delete=models.CASCADE, related_name='collector')
    # pass_code = models.CharField(max_length=6)

    def __str__(self):
        return self.user.email
