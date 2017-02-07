# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_link', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, default='')),
                ('profile', models.CharField(max_length=200, default='Parkinson')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, default='')),
                ('profile', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('phase_I_duration', models.CharField(max_length=200)),
                ('phase_I_content', models.CharField(max_length=200, default='min')),
                ('phase_II_duration', models.CharField(max_length=200)),
                ('phase_II_content', models.CharField(max_length=200, default='min')),
                ('phase_III_duration', models.CharField(max_length=200)),
                ('phase_III_content', models.CharField(max_length=200, default='min')),
                ('phase_IV_duration', models.CharField(max_length=200)),
                ('phase_IV_content', models.CharField(max_length=200, default='min')),
                ('phase_V_duration', models.CharField(max_length=200)),
                ('phase_V_content', models.CharField(max_length=200, default='min')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(to='mParkCore.Patient', related_name='sessions')),
                ('professional', models.ForeignKey(to='mParkCore.Professional', related_name='sessions')),
            ],
        ),
        migrations.CreateModel(
            name='SessionFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('file', models.FileField(upload_to='uploads')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(to='mParkCore.Patient', related_name='session_files')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='professional',
            name='team',
            field=models.ForeignKey(to='mParkCore.Team', related_name='professionals'),
        ),
        migrations.AddField(
            model_name='professional',
            name='user',
            field=models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='mParkCore.Post', related_name='comments'),
        ),
        migrations.AddField(
            model_name='carelinks',
            name='patient',
            field=models.ForeignKey(to='mParkCore.Patient', related_name='patients'),
        ),
        migrations.AddField(
            model_name='carelinks',
            name='professional',
            field=models.ForeignKey(to='mParkCore.Professional', related_name='professionals'),
        ),
    ]
