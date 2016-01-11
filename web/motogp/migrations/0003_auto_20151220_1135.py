# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0002_auto_20151220_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='latitude',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='country',
            name='longitude',
            field=models.CharField(max_length=255),
        ),
    ]
