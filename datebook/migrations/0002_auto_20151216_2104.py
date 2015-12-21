# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='company',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='move',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='men',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='move',
            name='move_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='move',
            name='pk_ld_del',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='move',
            name='remarks',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='move',
            name='type',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
