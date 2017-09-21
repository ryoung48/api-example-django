# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0005_auto_20170919_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 18, 22, 0, 730000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 18, 22, 0, 730000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'N', b''), (b'A', b'Arrived'), (b'Ci', b'Checked-in'), (b'Ir', b'In Room'), (b'Ca', b'Cancelled'), (b'F', b'Complete'), (b'C', b'Confirmed'), (b'Is', b'In Session'), (b'Ns', b'No Show'), (b'Nc', b'Not Confirmed'), (b'R', b'Rescheduled')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 18, 22, 0, 729000, tzinfo=utc)),
        ),
    ]
