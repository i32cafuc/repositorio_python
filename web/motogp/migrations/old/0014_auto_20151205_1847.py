# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0013_auto_20151123_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='circuito',
        ),
        migrations.AddField(
            model_name='race',
            name='circuit',
            field=models.ForeignKey(default='default', to='motogp.Circuit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='name',
            field=models.CharField(default='defa', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='league',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='debut',
            field=models.BooleanField(default=True),
        ),
    ]
