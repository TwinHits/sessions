# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_character_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='campaign',
            field=models.ForeignKey(default=None, to='session.Campaign'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='campaign',
            field=models.ForeignKey(default=None, to='session.Campaign'),
            preserve_default=False,
        ),
    ]
