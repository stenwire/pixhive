# Generated by Django 5.1.2 on 2024-10-30 11:16

import django.db.models.deletion
import photo.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('collection', '0001_initial'),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=photo.models.generate_upload_path)),
                ('original_file_name', models.TextField()),
                ('file_name', models.CharField(max_length=255, unique=True)),
                ('file_type', models.CharField(max_length=255)),
                ('upload_finished_at', models.DateTimeField(blank=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hiver')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]