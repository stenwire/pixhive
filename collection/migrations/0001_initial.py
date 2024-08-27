# Generated by Django 5.1 on 2024-08-27 02:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('pass_code', models.CharField(blank=True, null=True, unique=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('is_purchased', models.BooleanField(default=False)),
                ('collection_url', models.URLField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='accounts.hiver')),
                ('purchased_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections', to='accounts.collector')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchasedCollection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('amount_paid', models.FloatField()),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_collection', to='collection.collection')),
                ('collector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_collection', to='accounts.collector')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]