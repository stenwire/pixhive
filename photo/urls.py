from django.urls import path

from .views import (
    GetDeleteImageView,
    GetImagesByCollectionView,
    UploadImageView,
)

urlpatterns = [
    path("upload/", UploadImageView.as_view(), name="upload_image"),
    path(
        "<uuid:image_id>/",
        GetDeleteImageView.as_view(),
        name="get_delete_image",
    ),
    # path("<uuid:image_id>/", DeleteImageView.as_view(), name="delete-image"),
    path(
        "collection/<uuid:collection_id>/",
        GetImagesByCollectionView.as_view(),
        name="get_images_by_collection",
    ),
]
