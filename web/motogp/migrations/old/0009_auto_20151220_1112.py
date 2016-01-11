# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0008_auto_20151220_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
