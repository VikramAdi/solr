# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('division', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('circle', models.CharField(max_length=100)),
                ('taluk', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
