# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ptype', models.CharField(unique=True, max_length=5)),
                ('pcost', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='projection',
            name='dimension',
            field=models.ForeignKey(to='website.ProjectionType'),
        ),
        migrations.AddField(
            model_name='projection',
            name='pmovie',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
