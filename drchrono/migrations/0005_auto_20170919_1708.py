# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170917_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='api_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='doctor',
            name='api_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='patient',
            name='api_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 17, 8, 24, 364000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 17, 8, 24, 364000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='wait_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 17, 8, 24, 362000, tzinfo=utc)),
        ),
    ]
