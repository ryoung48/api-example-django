# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0008_auto_20170919_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_ref',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='appointment',
            name='gender',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 36, 45, 985000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 36, 45, 985000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 36, 45, 983000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(default=b'', max_length=15),
        ),
    ]
