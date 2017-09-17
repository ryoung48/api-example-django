# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_appointment_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 17, 2, 2, 33, 32000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(default='O', max_length=1, choices=[(b'I', b'checked in'), (b'O', b'checked out'), (b'P', b'with patient')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 17, 2, 3, 16, 752000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'A', b'arrived'), (b'C', b'confirmed')]),
        ),
    ]
