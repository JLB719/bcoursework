# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0002_skillitem_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillitem',
            name='text',
        ),
        migrations.AddField(
            model_name='skillitem',
            name='skill',
            field=models.TextField(default=''),
        ),
    ]
