# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-11 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0010_emailitem_numberitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalProfileItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]