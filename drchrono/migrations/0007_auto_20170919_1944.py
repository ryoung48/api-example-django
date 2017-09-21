# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0006_auto_20170919_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='cell_phone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='home_phone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='patient',
            name='preferred_language',
            field=models.CharField(default=b'', max_length=3),
        ),
        migrations.AddField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(default=b'46032', max_length=15),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 44, 26, 325000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 44, 26, 325000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'N', b''), (b'A', b'Arrived'), (b'Ci', b'Checked In'), (b'Ir', b'In Room'), (b'Ca', b'Cancelled'), (b'F', b'Complete'), (b'C', b'Confirmed'), (b'Is', b'In Session'), (b'Ns', b'No Show'), (b'Nc', b'Not Confirmed'), (b'R', b'Rescheduled')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 44, 26, 323000, tzinfo=utc)),
        ),
    ]
