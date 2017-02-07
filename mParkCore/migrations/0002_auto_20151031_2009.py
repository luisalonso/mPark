# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mParkCore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='phase_III_content',
        ),
        migrations.RemoveField(
            model_name='session',
            name='phase_II_content',
        ),
        migrations.RemoveField(
            model_name='session',
            name='phase_IV_content',
        ),
        migrations.RemoveField(
            model_name='session',
            name='phase_I_content',
        ),
        migrations.RemoveField(
            model_name='session',
            name='phase_V_content',
        ),
        migrations.AddField(
            model_name='session',
            name='max_BPM',
            field=models.CharField(default='140', max_length=200),
        ),
        migrations.AddField(
            model_name='session',
            name='min_BPM',
            field=models.CharField(default='80', max_length=200),
        ),
    ]
