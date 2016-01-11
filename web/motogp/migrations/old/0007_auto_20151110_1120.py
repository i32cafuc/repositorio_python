# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0006_auto_20151110_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rider',
            name='uteam',
        ),
        migrations.AddField(
            model_name='uteam',
            name='rider',
            field=models.ManyToManyField(default=None, to='motogp.Rider', null=True, blank=True),
        ),
    ]
