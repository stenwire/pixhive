from rest_framework import serializers

from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["uuid", "name", "description", "created", "last_updated"]
        read_only_fields = ["uuid", "created", "last_updated"]
