# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0005_auto_20200805_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillitem',
            old_name='skill',
            new_name='text',
        ),
    ]