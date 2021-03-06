# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('tweet_detail', models.TextField(max_length=140)),
                ('location', models.CharField(max_length=200)),
                ('followers', models.IntegerField(default=0)),
                ('status_number', models.IntegerField(default=0)),
                ('sentiment', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Neutral', 'Neutral')], default='Neutral', max_length=15)),
                ('mentioned_clergy', models.ManyToManyField(to='entry.Clergy')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('username', models.CharField(max_length=400, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.User'),
        ),
    ]
