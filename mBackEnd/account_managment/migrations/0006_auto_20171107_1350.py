# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_managment', '0005_userrestorecode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrestorecode',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserRestoreCode',
        ),
    ]
