# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0007_auto_20141029_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='super_subject',
            field=models.ForeignKey(default=None, blank=True, to='quest_viewer.Subject', null=True),
            preserve_default=True,
        ),
    ]
