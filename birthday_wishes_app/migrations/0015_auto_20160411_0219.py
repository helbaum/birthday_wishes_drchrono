# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 09:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes_app', '0014_auto_20160411_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='expires_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 9, 19, 0, 459274, tzinfo=utc)),
        ),
    ]
