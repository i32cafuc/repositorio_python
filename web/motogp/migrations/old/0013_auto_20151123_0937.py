# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0012_auto_20151117_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='league',
        ),
        migrations.RemoveField(
            model_name='uteam',
            name='point',
        ),
        migrations.AddField(
            model_name='uteam',
            name='league',
            field=models.ForeignKey(default=None, blank=True, to='motogp.League', null=True),
        ),
    ]
