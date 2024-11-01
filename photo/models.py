from django.db import models

from accounts.models import Hiver
from collection.models import Collection
from utils.models import TrackObjectStateMixin


def generate_upload_path(instance, filename):
    # file_name = instance.file_name
    # file_uuid = instance.uuid
    collection = instance.collection.uuid
    # created_at = timezone.now().strftime("%Y-%m-%dT%H:%M:%S")
    return f"images/{collection}/{filename}"


class Images(TrackObjectStateMixin):
    file = models.FileField(
        upload_to=generate_upload_path, blank=True, null=True, max_length=255
    )
    file_url = models.CharField(max_length=255, blank=True, null=True)
    original_file_name = models.TextField()
    file_name = models.CharField(max_length=255, unique=True)
    file_type = models.CharField(max_length=255)
    upload_finished_at = models.DateTimeField(blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(Hiver, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.file_name}"

    @property
    def is_valid(self):
        return bool(self.upload_finished_at)
