# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=11, decimal_places=2)),
                ('salary', models.DecimalField(max_digits=11, decimal_places=2)),
                ('point', models.IntegerField(default=0)),
                ('on_sale', models.BooleanField(default=0)),
                ('damage', models.BooleanField(default=0)),
                ('image', models.CharField(max_length=255)),
                ('image_dir', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('min_price', models.DecimalField(max_digits=11, decimal_places=2)),
                ('image', models.CharField(max_length=255)),
                ('image_dir', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='motogp.Category')),
            ],
        ),
        migrations.AddField(
            model_name='rider',
            name='team',
            field=models.ForeignKey(to='motogp.Team'),
        ),
    ]
