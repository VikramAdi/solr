# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=20)),
                ('synonym_1', models.CharField(max_length=30, blank=True)),
                ('synonym_2', models.CharField(max_length=30, blank=True)),
                ('synonym_3', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('pic', models.ImageField(null=True, upload_to=products.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecs',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='products.Product')),
                ('frnd_name', models.CharField(max_length=30, verbose_name=b'common name')),
                ('scientific_name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.TextField()),
            ],
            bases=('products.product',),
        ),
        migrations.AddField(
            model_name='productpic',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
