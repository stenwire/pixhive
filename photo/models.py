from django.db import models
from utils.models import TrackObjectStateMixin
from collection.models import Collection
# Create your models here.

class Photo(TrackObjectStateMixin):
  name = models.CharField(max_length=255)
  collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"{self.name} - {self.collection.name}"
