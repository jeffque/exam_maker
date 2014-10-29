# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0002_auto_20141028_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinessubject',
            name='main_discipline',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionsubject',
            name='main_subject',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
