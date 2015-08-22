# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('completed', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.CharField(unique=True, max_length=10)),
                ('level', models.IntegerField()),
                ('text', models.TextField()),
                ('question_image', models.ImageField(upload_to=b'/image/')),
                ('oth', models.ForeignKey(to='main.OTH')),
            ],
        ),
        migrations.CreateModel(
            name='UserOTHStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='oth',
            name='user_oth_status',
            field=models.ForeignKey(to='main.UserOTHStatus'),
        ),
    ]
