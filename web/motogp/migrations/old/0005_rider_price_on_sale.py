# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0004_remove_rider_on_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='price_on_sale',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
            preserve_default=False,
        ),
    ]
