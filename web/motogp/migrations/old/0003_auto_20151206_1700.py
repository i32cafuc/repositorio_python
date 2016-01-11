# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0002_auto_20151206_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='rider_on_sale',
            field=models.ManyToManyField(default=None, to='motogp.Rider', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='uteam',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
