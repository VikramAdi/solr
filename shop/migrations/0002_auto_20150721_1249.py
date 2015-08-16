# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
    ]
