# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0009_auto_20151110_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='uteam',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
