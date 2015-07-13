# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Campaign Name', max_length=255)),
                ('date', models.DateTimeField(verbose_name='Start Date')),
                ('system', models.CharField(default=None, max_length=255, choices=[('Star Wars: D6', 'Star Wars: D6'), ('Dungeons and Dragons: 5th Edition', 'Dungeons and Dragons: 5th Edition'), ('Dungeons and Dragons: 4th Edition', 'Dungeons and Dragons: 4th Edition'), ('Star Wars: Edge Of Empire', 'Star Wars: Edge Of Empire'), ('Deadlands', 'Deadlands')])),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Character Name', max_length=255)),
                ('campaign', models.ForeignKey(to='notes.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(verbose_name='Note', max_length=1000)),
                ('date', models.DateTimeField(verbose_name='Date Taken')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(verbose_name='Session Date')),
                ('campaign', models.ForeignKey(to='notes.Campaign')),
            ],
        ),
    ]
