# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0007_auto_20151110_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uteam',
            name='loan',
            field=models.BooleanField(default=0),
        ),
    ]
