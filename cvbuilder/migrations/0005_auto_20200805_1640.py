# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0004_auto_20200805_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillitem',
            old_name='text',
            new_name='skill',
        ),
    ]
