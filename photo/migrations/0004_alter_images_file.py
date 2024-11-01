# Generated by Django 5.1.2 on 2024-10-31 17:48

import photo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_rename_file_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=photo.models.generate_upload_path),
        ),
    ]
