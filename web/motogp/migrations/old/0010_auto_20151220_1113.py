# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0009_auto_20151220_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('iso3', models.CharField(max_length=255)),
                ('color_fill', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=5, decimal_places=2)),
                ('longitude', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='country',
            field=models.ForeignKey(default='', to='motogp.Country'),
            preserve_default=False,
        ),
    ]
