from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone

from photo.models import Images, generate_upload_path

from .local_storage_service import upload_file_to_local
from .s3_service import delete_image_from_s3, upload_file_to_s3


def upload_image(file, image_instance, storage_type):
    file_path = generate_upload_path(image_instance, image_instance.file_name)
    print(f"file_path: {file_path}")
    storage_type = settings.FILE_UPLOAD_STORAGE
    if storage_type == "s3":
        file_url = upload_file_to_s3(file, file_path)
        image_instance.file_url = file_url
    else:
        file_url = (
            f"{settings.APP_DOMAIN}{upload_file_to_local(file, file_path)}"
        )
        image_instance.file_url = None

    # if file_url:
    image_instance.file = file_url
    image_instance.upload_finished_at = timezone.now()
    image_instance.save()
    return file_url


def get_image(image_uuid):
    return Images.objects.get(uuid=image_uuid)


def get_images_by_collection(collection_id):
    return Images.objects.filter(collection_id=collection_id)


def delete_image(image_uuid, user):
    # Ensure that the user owns the image
    image = get_object_or_404(
        Images, uuid=image_uuid, uploaded_by=user.hiver.uuid
    )

    # Extract the S3 key from file_url
    file_url = image.file_url
    if file_url:
        file_path = file_url.split(
            f"https://{settings.AWS_CONFIG.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
        )[-1]
        print(f"file_path from delete: {file_path}")
        delete_image_from_s3(file_path)

    # Delete the image record from the database
    image.delete()
    return True
