# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 07:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes_app', '0013_auto_20160410_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readymessage',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='birthday_msg',
        ),
        migrations.AddField(
            model_name='patient',
            name='message',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='patient',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='expires_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 7, 33, 37, 67987, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='ReadyMessage',
        ),
    ]