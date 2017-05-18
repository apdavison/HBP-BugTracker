# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=b'', max_length=200)),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ctx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collab', models.CharField(max_length=1024)),
                ('ctx', models.CharField(max_length=1024)),
                ('project_name', models.CharField(default=b'no_name', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('text', models.TextField(help_text=b'formatted using ReST')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=b'', max_length=12)),
                ('author', models.CharField(default=b'', max_length=200)),
                ('ctx', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='issuetracker.Ctx')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='issuetracker.Ticket'),
        ),
    ]
