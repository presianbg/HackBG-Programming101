# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150521_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projection',
            old_name='pmovie',
            new_name='movie',
        ),
    ]
