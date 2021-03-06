# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 05:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes_app', '0011_auto_20160410_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ready_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='expires_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 5, 19, 57, 270739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='msg_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ready_message',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='birthday_wishes_app.Patient'),
        ),
    ]
