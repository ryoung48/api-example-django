# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0010_auto_20170920_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='duration',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='appointment',
            name='exam_room',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='appointment',
            name='office',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 18, 10, 30, 849000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 18, 10, 30, 849000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 18, 10, 30, 847000, tzinfo=utc)),
        ),
    ]
