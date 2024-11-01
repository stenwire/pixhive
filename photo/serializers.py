from uuid import uuid4

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from accounts.models import Hiver
from collection.models import Collection
from photo.models import Images


class ImageUploadSerializer(serializers.ModelSerializer):
    collection_id = serializers.UUIDField(
        write_only=True
    )  # Required on input only
    # file = serializers.FileField()

    class Meta:
        model = Images
        fields = [
            "file",
            "file_url",
            "original_file_name",
            "file_name",
            "file_type",
            "collection_id",
            "uploaded_by",
        ]
        read_only_fields = [
            "file_name",
            "file_url",
            "file_type",
            "uploaded_by",
            "original_file_name",
        ]

    def validate_file(self, file):
        # Ensure file is provided and validate file size/type if needed
        max_file_size = 10 * 1024 * 1024  # 10MB max size
        if file.size > max_file_size:
            raise serializers.ValidationError(
                "File size exceeds the maximum limit of 10MB."
            )
        return file

    def validate_collection_id(self, collection_id):
        # Validate that the collection exists and is owned
        # by the current user's Hiver instance
        hiver = get_object_or_404(
            Hiver, user=self.context["request"].user.uuid
        )

        if not Collection.objects.filter(
            uuid=collection_id, owner=hiver.uuid
        ).exists():
            raise serializers.ValidationError(
                "Collection not found or you do not have access."
            )

        return collection_id

    def create(self, validated_data):
        # Auto-generate file_name and set file_type
        file = validated_data["file"]
        validated_data["original_file_name"] = file.name
        # validated_data['file_name'] = f"{
        # validated_data['uploaded_by'].uuid}_{file.name}"
        validated_data["file_name"] = f"{uuid4().hex}_{file.name}"
        validated_data["file_type"] = file.content_type

        return super().create(validated_data)


class ImageSerializer(serializers.ModelSerializer):
    # For fetching image data
    class Meta:
        model = Images
        fields = [
            "uuid",
            "file",
            "file_url",
            "file_name",
            "file_type",
            "collection",
            "uploaded_by",
            "upload_finished_at",
        ]
        read_only_fields = fields  # All fields read-only for fetching


class ImageDeleteSerializer(serializers.Serializer):
    image_uuid = serializers.UUIDField()

    def validate_image_uuid(self, image_uuid):
        hiver = get_object_or_404(
            Hiver, user=self.context["request"].user.uuid
        )

        if not Images.objects.filter(
            uuid=image_uuid, uploaded_by=hiver.uuid
        ).exists():
            raise serializers.ValidationError(
                "Image not found or you do not have access."
            )

        return image_uuid
