# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0011_rider_valuation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='min_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='uteam',
            name='coin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='uteam',
            name='owe',
            field=models.IntegerField(default=0),
        ),
    ]
