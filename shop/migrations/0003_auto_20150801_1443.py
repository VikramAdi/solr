# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150721_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='delivery_areas',
            field=models.ManyToManyField(to='address.Address', null=True, blank=True),
        ),
    ]
