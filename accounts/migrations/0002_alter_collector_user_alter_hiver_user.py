# Generated by Django 5.1.2 on 2024-10-31 15:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='collector', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hiver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
