# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0008_auto_20141030_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institute',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objectiveoptionitem',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionsubject',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment', blank=True),
            preserve_default=True,
        ),
    ]
