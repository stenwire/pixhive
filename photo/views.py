from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Hiver
from services.image_service import (
    delete_image,
    get_image,
    get_images_by_collection,
    upload_image,
)

from .models import Images
from .serializers import (
    ImageSerializer,
    ImageUploadSerializer,
)


class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImageUploadSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            # hiver = Hiver.get_object(uuid=request.user.uuid)
            print(f"Logged in user id: {request.user.uuid}")
            hiver = get_object_or_404(Hiver, user=request.user.uuid)

            serializer.save(uploaded_by=hiver)
            storage_type = settings.FILE_UPLOAD_STORAGE
            file_url = upload_image(
                request.FILES["file"],
                serializer.instance,
                storage_type=storage_type,
            )
            print(f"file_url: {file_url}")
            if file_url:
                return Response(
                    {"file_url": file_url}, status=status.HTTP_201_CREATED
                )
            return Response(
                {"error": "Upload failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDeleteImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        try:
            image = get_image(image_id)
            serializer = ImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Images.DoesNotExist:
            return Response(
                {"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, image_id):
        # Call the delete_image function with the provided image_id
        delete_image(image_id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DeleteImageView(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, image_id):
#         # Call the delete_image function with the provided image_id
#         delete_image(image_id, request.user)
#         return Response(status=status.HTTP_204_NO_CONTENT)


class GetImagesByCollectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, collection_id):
        images = get_images_by_collection(collection_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
