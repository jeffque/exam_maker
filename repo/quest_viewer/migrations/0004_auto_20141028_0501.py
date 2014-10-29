# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0003_auto_20141028_0456'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commentary',
            new_name='Comment',
        ),
        migrations.AddField(
            model_name='answer',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discipline',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institute',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='objectiveoptionitem',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionsubject',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='comments',
            field=models.ManyToManyField(to='quest_viewer.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='super_subject',
            field=models.ForeignKey(default=None, blank=True, to='quest_viewer.Subject'),
            preserve_default=True,
        ),
    ]
