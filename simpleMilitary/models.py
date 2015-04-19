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
    psin = models.ForeignKey('Personnel', db_column='PSIN', blank=True, null=True)  # Field name made lowercase.
    serialno = models.ForeignKey('Equipment', db_column='SERIALNO', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        unique_together = ('psin', 'serialno')
        db_table = 'AUTHORIZED_TO_USE'


class Award(models.Model):
    code = models.IntegerField(db_column='CODE', primary_key=True)  # Field name made lowercase.
    aname = models.CharField(db_column='ANAME', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'AWARD'

    def __unicode__(self):
        return (self.aname)



class AwardedTo(models.Model):
    sin = models.ForeignKey('Person', db_column='SIN', blank=True, null=True)  # Field name made lowercase.
    code = models.ForeignKey(Award, db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        unique_together = ('sin', 'code')
        db_table = 'AWARDED_TO'

class Base(models.Model):
    bid = models.CharField(db_column='BID', primary_key=True, max_length=5)  # Field name made lowercase.
    bname = models.CharField(db_column='BNAME', max_length=30, verbose_name='Base')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=30, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'BASE'

    def __unicode__(self):
        return (self.bname)



class Conflict(models.Model):
    cid = models.CharField(db_column='CID', primary_key=True, max_length=5)  # Field name made lowercase.
    cname = models.CharField(db_column='CNAME', max_length=30, verbose_name='Conflict')  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'CONFLICT'

    def __unicode__(self):
        return (self.cname)



class Equipment(models.Model):
    serialno = models.CharField(db_column='SERIALNO', primary_key=True, max_length=5)  # Field name made lowercase.
    ename = models.CharField(db_column='ENAME', max_length=30, blank=True, verbose_name='Name')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=30, blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    bid = models.ForeignKey(Base, db_column='BID', blank=True, null=True)  # Field name made lowercase.
    cid = models.ForeignKey(Conflict, db_column='CID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        db_table = 'EQUIPMENT'

    def __unicode__(self):
        return (self.ename + "-" + self.serialno)



class Operations(models.Model):
    cid = models.ForeignKey(Conflict, db_column='CID', blank=True, null=True)  # Field name made lowercase.
    oname = models.CharField(db_column='ONAME', max_length=30, blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'Operations'
        verbose_name_plural = 'Operations'
        unique_together = ('cid', 'oname')
        db_table = 'OPERATIONS'

    def __unicode__(self):
        return (self.oname + "-" + self.cid.cname)


class Person(models.Model):
    sin = models.CharField(db_column='SIN', primary_key=True, max_length=9, verbose_name='Name')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FNAME', max_length=15, verbose_name="Name")  # Field name made lowercase.
    lname = models.CharField(db_column='LNAME', max_length=15)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True)  # Field name made lowercase.
    bdate = models.DateField(db_column='BDATE', blank=True, null=True)  # Field name made lowercase.
    enlist_date = models.DateField(db_column='ENLIST_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        db_table = 'PERSON'

    def __unicode__(self):
        return (self.sin)

    short_description = 'Name'


class Personnel(models.Model):
    psin = models.ForeignKey(Person, db_column='PSIN', primary_key=True, verbose_name='SIN')  # Field name made lowercase.
    rank = models.CharField(db_column='RANK', max_length=30, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=30)  # Field name made lowercase.
    uid = models.ForeignKey('Unit', db_column='UID', blank=True, null=True, verbose_name='Unit')  # Field name made lowercase.
    supersin = models.ForeignKey('self', db_column='SUPERSIN', blank=True, null=True, verbose_name='Supervisor')  # Field name made lowercase.
    class Meta:
        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnel'
        db_table = 'PERSONNEL'
    short_description = 'Name'

    def __unicode__(self):
        return (self.psin.fname + " " + self.psin.lname)

    def get_fname(self):
        return u'%s' % self.psin.fname

    def get_name(self):
        return u'%s' % (self.psin.fname + " " + self.psin.lname)

    def get_lname(self):
        return u'%s' % self.psin.lname

    def get_sin(self):
        try:
            return u'%s' % self.psin
        except Person.DoesNotExist:
            return u'No Person'

    get_name.short_description = 'Name'
    get_fname.short_description = 'First Name'  #Renames column head
    get_lname.short_description = 'Last Name'  #Renames column head
    get_sin.short_description = 'SIN'  #Renames column head


class Unit(models.Model):
    uid = models.CharField(db_column='UID', primary_key=True, max_length=5)  # Field name made lowercase.
    uname = models.CharField(db_column='UNAME', max_length=40, verbose_name='Unit')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True)  # Field name made lowercase.
    bid = models.ForeignKey(Base, db_column='BID', blank=True, null=True, verbose_name="Base")  # Field name made lowercase.
    cid = models.ForeignKey(Conflict, db_column='CID', blank=True, null=True, verbose_name="Conflict")  # Field name made lowercase.
    commander_sin = models.ForeignKey(Personnel, db_column='COMMANDER_SIN', blank=True, null=True, verbose_name='Commander SIN')  # Field name made lowercase.

    class Meta:
        db_table = 'UNIT'


    def get_bname(self):
        if self.bid is not None:
            return self.bid.bname
        else:
            return ""

    def get_cname(self):
        if self.cid is not None:
            return self.cid.cname
        else:
            return ""

    get_cname.short_description = 'Conflict'  #Renames column head
    get_bname.short_description = 'Base'  #Renames column head



class Veteran(models.Model):
    vsin = models.ForeignKey(Person, db_column='VSIN', primary_key=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'VETERAN'

    def __unicode__(self):
        return (self.vsin)

