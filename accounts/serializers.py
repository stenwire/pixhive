from models import Hiver
from rest_framework import serializers


class HiverSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Hiver
        field = "__all__"
        read_only_fields = ["uuid", "created", "last_updated"]
