# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectiontype',
            name='pcost',
            field=models.PositiveSmallIntegerField(verbose_name='Price for ticket (BGN)'),
        ),
        migrations.AlterField(
            model_name='projectiontype',
            name='ptype',
            field=models.CharField(verbose_name='Dimension', unique=True, max_length=5),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together=set([('projection', 'row', 'col')]),
        ),
    ]
