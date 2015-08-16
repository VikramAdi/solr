# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
