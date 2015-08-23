# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oth_id', models.CharField(unique=True, max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('duration', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'OTH',
                'verbose_name_plural': 'OTHs',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.CharField(unique=True, max_length=10)),
                ('level', models.IntegerField()),
                ('text', models.TextField()),
                ('question_image', models.ImageField(upload_to=main.models.update_image_name, blank=True)),
                ('answer', models.CharField(max_length=100)),
                ('oth', models.ForeignKey(to='main.OTH')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='UserOTHStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('oth', models.ForeignKey(to='main.OTH')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User OTH Status',
                'verbose_name_plural': 'User OTH Statuses',
            },
        ),
    ]
