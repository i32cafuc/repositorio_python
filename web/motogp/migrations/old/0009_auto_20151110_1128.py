# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0008_auto_20151110_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uteam',
            old_name='due',
            new_name='owe',
        ),
    ]
