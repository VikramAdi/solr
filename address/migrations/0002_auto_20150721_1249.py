# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 12, 47, 42, 311160, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
    ]
