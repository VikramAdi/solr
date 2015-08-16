# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('categories', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpic',
            name='shop',
            field=models.ForeignKey(to='shop.Shop'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='categories.Catalog'),
        ),
    ]
