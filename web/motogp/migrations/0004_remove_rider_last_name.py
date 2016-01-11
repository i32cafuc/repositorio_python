# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0003_auto_20151220_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rider',
            name='last_name',
        ),
    ]
