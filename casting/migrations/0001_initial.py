# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('avatar_url', models.URLField(null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=200, null=True, blank=True)),
                ('hietanen', models.ForeignKey(related_query_name=b'hietanen', related_name='hietanen', to='casting.Actor', null=True)),
                ('kaarna', models.ForeignKey(related_query_name=b'kaarna', related_name='kaarna', to='casting.Actor', null=True)),
                ('kariluoto', models.ForeignKey(related_query_name=b'kariluoto', related_name='kariluoto', to='casting.Actor', null=True)),
                ('koskela', models.ForeignKey(related_query_name=b'koskela', related_name='koskela', to='casting.Actor', null=True)),
                ('lahtinen', models.ForeignKey(related_query_name=b'lahtinen', related_name='lahtinen', to='casting.Actor', null=True)),
                ('lammio', models.ForeignKey(related_query_name=b'lammio', related_name='lammio', to='casting.Actor', null=True)),
                ('lehto', models.ForeignKey(related_query_name=b'lehto', related_name='lehto', to='casting.Actor', null=True)),
                ('maatta', models.ForeignKey(related_query_name=b'maatta', related_name='maatta', to='casting.Actor', null=True)),
                ('rahikainen', models.ForeignKey(related_query_name=b'rahikainen', related_name='rahikainen', to='casting.Actor', null=True)),
                ('rokka', models.ForeignKey(related_query_name=b'rokka', related_name='rokka', to='casting.Actor', null=True)),
                ('sarastie', models.ForeignKey(related_query_name=b'sarastie', related_name='sarastie', to='casting.Actor', null=True)),
            ],
        ),
    ]
