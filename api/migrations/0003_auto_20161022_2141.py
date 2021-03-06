# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161022_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='in_continuum_of_care',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='in_shelter',
            field=models.BooleanField(default=False),
        ),
    ]
