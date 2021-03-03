from django.db import models

# Create your models here.

class train_user(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(db_column='nickname', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    power = models.CharField(db_column='power', max_length=32, blank=True, null=True)  # Field name made lowercase.
    jifen = models.IntegerField(db_column='jifen', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'train_user'


class match_results(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    a1 = models.CharField(db_column='a1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a2 = models.CharField(db_column='a2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b1 = models.CharField(db_column='b1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b2 = models.CharField(db_column='b2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    zongbifen = models.CharField(db_column='zongbifen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    meijubifen = models.CharField(db_column='meijubifen', max_length=128, blank=True, null=True)  # Field name made lowercase.
    shengli1 = models.CharField(db_column='shengli1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    shengli2 = models.CharField(db_column='shengli2', max_length=32, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'match_results'



