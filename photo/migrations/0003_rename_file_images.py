# Generated by Django 5.1.2 on 2024-10-31 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('collection', '0001_initial'),
        ('photo', '0002_file_delete_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='Images',
        ),
    ]
