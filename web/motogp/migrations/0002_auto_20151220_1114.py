# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0001_initial'),
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
        migrations.RemoveField(
            model_name='rider',
            name='on_sale',
        ),
        migrations.RemoveField(
            model_name='uteam',
            name='league',
        ),
        migrations.AddField(
            model_name='league',
            name='rider_on_sale',
            field=models.ManyToManyField(default=None, to='motogp.Rider', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='price_on_sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='league',
            field=models.ForeignKey(default=None, blank=True, to='motogp.League', null=True),
        ),
        migrations.AddField(
            model_name='uteam',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rider',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rider',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='country',
            field=models.ForeignKey(default=1, to='motogp.Country'),
            preserve_default=False,
        ),
    ]
