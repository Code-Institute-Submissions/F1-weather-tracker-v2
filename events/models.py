from django.db import models


class Event(models.Model):
    event = models.OneToOneField('Track', models.DO_NOTHING, primary_key=True)
    year = models.IntegerField()
    country = models.CharField(max_length=99, blank=True, null=True)
    city = models.CharField(max_length=99, blank=True, null=True)
    track_name = models.CharField(max_length=99, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    track_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Event'


class Track(models.Model):
    track_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=99, blank=True, null=True)
    city = models.CharField(max_length=99, blank=True, null=True)
    track_name = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Track'
