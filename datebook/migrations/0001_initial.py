# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('move_date', models.DateTimeField(blank=True, null=True)),
                ('company', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=10)),
                ('pk_ld_del', models.CharField(max_length=10)),
                ('weight_rooms', models.CharField(max_length=6)),
                ('men', models.CharField(max_length=4)),
                ('customer', models.CharField(max_length=20)),
                ('origin', models.CharField(max_length=15)),
                ('destination', models.CharField(max_length=15)),
                ('remarks', models.CharField(max_length=15)),
                ('details', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cancelled_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
