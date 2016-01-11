# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0005_rider_price_on_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rider',
            name='price_on_sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rider',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
