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
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
            ],
            options={
                'db_table': 'AUTHORIZED_TO_USE',
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AwardedTo',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('code', models.ForeignKey(db_column='CODE', blank=True, to='simpleMilitary.Award', null=True)),
            ],
            options={
                'db_table': 'AWARDED_TO',
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
                ('bid', models.ForeignKey(db_column='BID', blank=True, to='simpleMilitary.Base', null=True)),
                ('cid', models.ForeignKey(db_column='CID', blank=True, to='simpleMilitary.Conflict', null=True)),
            ],
            options={
                'db_table': 'EQUIPMENT',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('oname', models.CharField(max_length=30, db_column='ONAME', blank=True)),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('cid', models.ForeignKey(db_column='CID', blank=True, to='simpleMilitary.Conflict', null=True)),
            ],
            options={
                'db_table': 'OPERATIONS',
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('psin', models.ForeignKey(primary_key=True, db_column='PSIN', serialize=False, to='simpleMilitary.Person')),
                ('rank', models.CharField(max_length=30, db_column='RANK', blank=True)),
                ('status', models.CharField(max_length=30, db_column='STATUS')),
                ('supersin', models.ForeignKey(db_column='SUPERSIN', blank=True, to='simpleMilitary.Personnel', null=True)),
            ],
            options={
                'db_table': 'PERSONNEL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('uid', models.CharField(max_length=5, serialize=False, primary_key=True, db_column='UID')),
                ('uname', models.CharField(max_length=40, db_column='UNAME')),
                ('type', models.CharField(max_length=30, db_column='TYPE', blank=True)),
                ('bid', models.ForeignKey(db_column='BID', blank=True, to='simpleMilitary.Base', null=True)),
                ('cid', models.ForeignKey(db_column='CID', blank=True, to='simpleMilitary.Conflict', null=True)),
                ('commander_sin', models.ForeignKey(db_column='COMMANDER_SIN', blank=True, to='simpleMilitary.Personnel', null=True)),
            ],
            options={
                'db_table': 'UNIT',
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
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personnel',
            name='uid',
            field=models.ForeignKey(db_column='UID', blank=True, to='simpleMilitary.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='operations',
            unique_together=set([('cid', 'oname')]),
        ),
        migrations.AddField(
            model_name='awardedto',
            name='sin',
            field=models.ForeignKey(db_column='SIN', blank=True, to='simpleMilitary.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='awardedto',
            unique_together=set([('sin', 'code')]),
        ),
        migrations.AddField(
            model_name='authorizedtouse',
            name='psin',
            field=models.ForeignKey(db_column='PSIN', blank=True, to='simpleMilitary.Personnel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorizedtouse',
            name='serialno',
            field=models.ForeignKey(db_column='SERIALNO', blank=True, to='simpleMilitary.Equipment', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='authorizedtouse',
            unique_together=set([('psin', 'serialno')]),
        ),
    ]
