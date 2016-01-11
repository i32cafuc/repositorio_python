# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motogp', '0005_auto_20151109_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuit',
            name='image_dir',
        ),
        migrations.RemoveField(
            model_name='rider',
            name='image_dir',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_dir',
        ),
        migrations.RemoveField(
            model_name='team',
            name='min_price',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='test',
        ),
        migrations.AddField(
            model_name='rider',
            name='uteam',
            field=models.ManyToManyField(to='motogp.Uteam'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='debut',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='league',
            field=models.ForeignKey(default=None, blank=True, to='motogp.League', null=True),
        ),
        migrations.AddField(
            model_name='uteam',
            name='coin',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
        ),
        migrations.AddField(
            model_name='uteam',
            name='due',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
        ),
        migrations.AddField(
            model_name='uteam',
            name='enrolment',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='uteam',
            name='loan',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
        ),
        migrations.AddField(
            model_name='uteam',
            name='maintenance',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='min_price',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='image',
            field=models.ImageField(null=True, upload_to=b'circuits', blank=True),
        ),
        migrations.AlterField(
            model_name='rider',
            name='image',
            field=models.ImageField(null=True, upload_to=b'riders', blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(null=True, upload_to=b'teams', blank=True),
        ),
    ]
