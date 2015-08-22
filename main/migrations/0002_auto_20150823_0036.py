# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oth',
            options={'verbose_name': 'OTH', 'verbose_name_plural': 'OTHs'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='userothstatus',
            options={'verbose_name': 'User OTH Status', 'verbose_name_plural': 'User OTH Statuses'},
        ),
        migrations.AddField(
            model_name='oth',
            name='started',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oth',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
