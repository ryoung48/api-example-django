# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0009_auto_20170920_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_ref',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='gender',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 44, 5, 160000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 44, 5, 160000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 44, 5, 158000, tzinfo=utc)),
        ),
    ]
