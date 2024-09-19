# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Games(models.Model):
    author = models.ForeignKey('Users', models.DO_NOTHING, db_column='author')
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Statchanges(models.Model):
    gameid = models.OneToOneField(Games, models.DO_NOTHING, db_column='gameid', primary_key=True)  # The composite primary key (gameid, userid) found, that is not supported. The first column is selected.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    elo = models.IntegerField(blank=True, null=True)
    redbull = models.IntegerField(blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statchanges'
        unique_together = (('gameid', 'userid'),)


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pfp = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    elo = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    plays = models.IntegerField(blank=True, null=True)
    redbull = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
