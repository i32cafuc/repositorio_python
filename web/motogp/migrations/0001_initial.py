# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('min_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'circuits', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date_race', models.DateField()),
                ('date_block', models.DateField()),
                ('circuit', models.ForeignKey(to='motogp.Circuit')),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=11, decimal_places=2)),
                ('salary', models.DecimalField(max_digits=11, decimal_places=2)),
                ('point', models.IntegerField(default=0)),
                ('valuation', models.IntegerField(default=0)),
                ('on_sale', models.BooleanField(default=0)),
                ('damage', models.BooleanField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'riders', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'teams', blank=True)),
                ('category', models.ForeignKey(to='motogp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debut', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Uteam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('coin', models.IntegerField(default=0)),
                ('owe', models.IntegerField(default=0)),
                ('loan', models.BooleanField(default=0)),
                ('maintenance', models.BooleanField(default=0)),
                ('enrolment', models.BooleanField(default=0)),
                ('league', models.ForeignKey(default=None, blank=True, to='motogp.League', null=True)),
                ('rider', models.ManyToManyField(default=None, to='motogp.Rider', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uteam',
            field=models.ForeignKey(default=None, blank=True, to='motogp.Uteam', null=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='team',
            field=models.ForeignKey(to='motogp.Team'),
        ),
    ]
