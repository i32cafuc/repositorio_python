# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uteam',
            name='league',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='league',
            field=models.ForeignKey(default=None, blank=True, to='motogp.League', null=True),
        ),
    ]
