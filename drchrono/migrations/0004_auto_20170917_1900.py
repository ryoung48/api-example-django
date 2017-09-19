# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0003_auto_20170916_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='wait_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'A', b'arrived'), (b'C', b'confirmed'), (b'F', b'finished')]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'I', b'checked-in'), (b'O', b'checked-out'), (b'P', b'with patient')]),
        ),
    ]
