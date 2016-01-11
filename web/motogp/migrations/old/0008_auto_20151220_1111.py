# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0007_auto_20151220_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuit',
            name='country',
        ),
        migrations.AddField(
            model_name='race',
            name='country',
            field=models.ForeignKey(default='', to='motogp.Country'),
            preserve_default=False,
        ),
    ]
