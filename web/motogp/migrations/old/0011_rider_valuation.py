# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0010_uteam_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='valuation',
            field=models.IntegerField(default=0),
        ),
    ]
