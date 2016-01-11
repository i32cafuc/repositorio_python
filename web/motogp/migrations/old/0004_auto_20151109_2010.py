# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0003_auto_20151109_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'profiles', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='uteam',
            field=models.ForeignKey(to='motogp.Uteam'),
        ),
    ]
