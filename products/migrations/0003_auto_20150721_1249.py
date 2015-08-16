# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150719_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=20, blank=True),
        ),
    ]
