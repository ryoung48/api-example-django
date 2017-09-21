# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0007_auto_20170919_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 45, 46, 140000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 45, 46, 140000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 19, 45, 46, 138000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
