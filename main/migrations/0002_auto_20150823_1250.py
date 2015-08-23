# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userothstatus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 12, 50, 3, 684752), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userothstatus',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 23, 12, 50, 19, 598483), auto_now=True),
            preserve_default=False,
        ),
    ]
