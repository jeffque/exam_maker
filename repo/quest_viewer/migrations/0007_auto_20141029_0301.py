# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0006_auto_20141028_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='acronym',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='super_subject',
            field=models.ForeignKey(default=None, to='quest_viewer.Subject', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textalias',
            name='textHTML',
            field=models.ForeignKey(to='quest_viewer.TextHTML', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textalias',
            name='textTeX',
            field=models.ForeignKey(to='quest_viewer.TextTeX', null=True),
            preserve_default=True,
        ),
    ]
