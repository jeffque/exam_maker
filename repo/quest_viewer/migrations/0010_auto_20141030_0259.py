# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0009_auto_20141030_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='acronym',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
