# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('wagtailcore', '0040_page_draft_title')]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr',
                 models.OneToOneField(
                     parent_link=True,
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
