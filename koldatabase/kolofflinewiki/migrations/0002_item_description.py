# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kolofflinewiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]