# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes_app', '0005_auto_20160409_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='pname',
        ),
    ]
