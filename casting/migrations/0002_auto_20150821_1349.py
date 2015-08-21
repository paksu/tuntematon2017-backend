# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='casting',
            options={'ordering': ('created_at',)},
        ),
    ]
