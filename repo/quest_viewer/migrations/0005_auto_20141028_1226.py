# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0004_auto_20141028_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='disiplines',
            new_name='disciplines',
        ),
    ]
