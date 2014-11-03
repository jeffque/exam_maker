# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0011_auto_20141102_2026'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='disciplinessubject',
            unique_together=set([('discipline', 'subject')]),
        ),
    ]
