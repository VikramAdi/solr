# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('categories', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20, blank=True)),
                ('pin_code', models.CharField(max_length=6)),
                ('address_line', models.CharField(max_length=150)),
                ('shop_registration_no', models.CharField(max_length=50)),
                ('shop_registration_img', models.ImageField(null=True, upload_to=shop.models.upload_path, blank=True)),
                ('tin_no', models.CharField(max_length=50, null=True, blank=True)),
                ('tin_img', models.ImageField(null=True, upload_to=shop.models.upload_path, blank=True)),
                ('pan_no', models.CharField(max_length=13)),
                ('pan_img', models.ImageField(null=True, upload_to=shop.models.upload_path, blank=True)),
                ('delivery_areas', models.ManyToManyField(to='address.Address')),
                ('products', models.ManyToManyField(to='products.Product')),
                ('served_categories', models.ManyToManyField(to='categories.Catalog')),
            ],
        ),
    ]
