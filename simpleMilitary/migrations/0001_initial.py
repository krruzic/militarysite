# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorizedToUse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'AUTHORIZED_TO_USE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True, db_column='CODE')),
                ('aname', models.CharField(max_length=30, db_column='ANAME', blank=True)),
            ],
            options={
                'db_table': 'AWARD',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AwardedTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'AWARDED_TO',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('bid', models.CharField(max_length=5, serialize=False, primary_key=True, db_column='BID')),
                ('bname', models.CharField(max_length=30, db_column='BNAME')),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
                ('location', models.CharField(max_length=30, db_column='LOCATION', blank=True)),
            ],
            options={
                'db_table': 'BASE',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conflict',
            fields=[
                ('cid', models.CharField(max_length=5, serialize=False, primary_key=True, db_column='CID')),
                ('cname', models.CharField(max_length=30, db_column='CNAME')),
                ('start_date', models.DateField(null=True, db_column='START_DATE', blank=True)),
                ('status', models.CharField(max_length=10, db_column='STATUS', blank=True)),
            ],
            options={
                'db_table': 'CONFLICT',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('serialno', models.CharField(max_length=5, serialize=False, primary_key=True, db_column='SERIALNO')),
                ('ename', models.CharField(max_length=30, db_column='ENAME', blank=True)),
                ('status', models.CharField(max_length=30, db_column='STATUS', blank=True)),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
            ],
            options={
                'db_table': 'EQUIPMENT',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oname', models.CharField(max_length=30, db_column='ONAME')),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
            ],
            options={
                'db_table': 'OPERATIONS',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('sin', models.CharField(max_length=9, serialize=False, primary_key=True, db_column='SIN')),
                ('address', models.CharField(max_length=50, db_column='ADDRESS', blank=True)),
                ('fname', models.CharField(max_length=15, db_column='FNAME')),
                ('lname', models.CharField(max_length=15, db_column='LNAME')),
                ('sex', models.CharField(max_length=1, db_column='SEX', blank=True)),
                ('bdate', models.DateField(null=True, db_column='BDATE', blank=True)),
                ('enlist_date', models.DateField(null=True, db_column='ENLIST_DATE', blank=True)),
            ],
            options={
                'db_table': 'PERSON',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('psin', models.ForeignKey(primary_key=True, db_column='PSIN', serialize=False, to='simpleMilitary.Person')),
                ('rank', models.CharField(max_length=30, db_column='RANK', blank=True)),
                ('status', models.CharField(max_length=30, db_column='STATUS')),
            ],
            options={
                'db_table': 'PERSONNEL',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('uid', models.CharField(max_length=5, serialize=False, primary_key=True, db_column='UID')),
                ('uname', models.CharField(max_length=40, db_column='UNAME')),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
            ],
            options={
                'db_table': 'UNIT',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Veteran',
            fields=[
                ('vsin', models.ForeignKey(primary_key=True, db_column='VSIN', serialize=False, to='simpleMilitary.Person')),
                ('end_date', models.DateField(null=True, db_column='END_DATE', blank=True)),
            ],
            options={
                'db_table': 'VETERAN',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
