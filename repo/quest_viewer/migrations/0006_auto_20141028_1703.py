# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_viewer', '0005_auto_20141028_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextHTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('images_url', models.ManyToManyField(to='quest_viewer.ImagesUrl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextTeX',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('images_url', models.ManyToManyField(to='quest_viewer.ImagesUrl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='textalias',
            name='textHTML',
            field=models.ForeignKey(to='quest_viewer.TextHTML', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textalias',
            name='textTeX',
            field=models.ForeignKey(to='quest_viewer.TextTeX', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.ForeignKey(to='quest_viewer.TextAlias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='objectiveoptionitem',
            name='item_text',
            field=models.ForeignKey(to='quest_viewer.TextAlias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.ForeignKey(to='quest_viewer.TextAlias'),
            preserve_default=True,
        ),
    ]
