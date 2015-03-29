# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthorizedToUse(models.Model):
    psin = models.ForeignKey('Personnel', db_column='PSIN')  # Field name made lowercase.
    serialno = models.ForeignKey('Equipment', db_column='SERIALNO')  # Field name made lowercase.

    class Meta:
        unique_together = ('psin', 'serialno')
        db_table = 'AUTHORIZED_TO_USE'


class Award(models.Model):
    code = models.IntegerField(db_column='CODE', primary_key=True)  # Field name made lowercase.
    aname = models.CharField(db_column='ANAME', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AWARD'


class AwardedTo(models.Model):
    sin = models.ForeignKey('Person', db_column='SIN')  # Field name made lowercase.
    code = models.ForeignKey(Award, db_column='CODE')  # Field name made lowercase.

    class Meta:
        unique_together = ('sin', 'code')        
        db_table = 'AWARDED_TO'


class Base(models.Model):
    bid = models.CharField(db_column='BID', primary_key=True, max_length=5, primary_key=True)  # Field name made lowercase.
    bname = models.CharField(db_column='BNAME', max_length=30)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'BASE'


class Conflict(models.Model):
    cid = models.CharField(db_column='CID', primary_key=True, max_length=5, primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='CNAME', max_length=30)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CONFLICT'


class Equipment(models.Model):
    serialno = models.CharField(db_column='SERIALNO', primary_key=True, max_length=5, primary_key=True)  # Field name made lowercase.
    ename = models.CharField(db_column='ENAME', max_length=30, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=30, blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    bid = models.ForeignKey(Base, db_column='BID', blank=True, null=True)  # Field name made lowercase.
    cid = models.ForeignKey(Conflict, db_column='CID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'EQUIPMENT'


class Operations(models.Model):
    cid = models.ForeignKey(Conflict, db_column='CID', primary_key=True)  # Field name made lowercase.
    oname = models.CharField(db_column='ONAME', max_length=30)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'OPERATIONS'


class Person(models.Model):
    sin = models.CharField(db_column='SIN', primary_key=True, max_length=9, primary_key=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FNAME', max_length=15)  # Field name made lowercase.
    lname = models.CharField(db_column='LNAME', max_length=15)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True)  # Field name made lowercase.
    bdate = models.DateField(db_column='BDATE', blank=True, null=True)  # Field name made lowercase.
    enlist_date = models.DateField(db_column='ENLIST_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PERSON'


class Personnel(models.Model):
    psin = models.ForeignKey(Person, db_column='PSIN', primary_key=True, primary_key=True)  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=30, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=30)  # Field name made lowercase.
    uid = models.ForeignKey('Unit', db_column='UID', blank=True, null=True)  # Field name made lowercase.
    supersin = models.ForeignKey('self', db_column='SUPERSIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PERSONNEL'


class Unit(models.Model):
    uid = models.CharField(db_column='UID', primary_key=True, max_length=5, primary_key=True)  # Field name made lowercase.
    uname = models.CharField(db_column='UNAME', max_length=40)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    bid = models.ForeignKey(Base, db_column='BID', blank=True, null=True)  # Field name made lowercase.
    cid = models.ForeignKey(Conflict, db_column='CID', blank=True, null=True)  # Field name made lowercase.
    commander_sin = models.ForeignKey(Personnel, db_column='COMMANDER_SIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UNIT'


class Veteran(models.Model):
    vsin = models.ForeignKey(Person, db_column='VSIN', primary_key=True, primary_key=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'VETERAN'
