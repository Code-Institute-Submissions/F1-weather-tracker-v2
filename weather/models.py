from django.db import models


# Create your models here.
class Schedule(models.Model):
    event_id = models.IntegerField(primary_key=True)
    practice1_start = models.CharField(max_length=16, blank=True, null=True)
    practice2_start = models.CharField(max_length=16, blank=True, null=True)
    practice3_start = models.CharField(max_length=16, blank=True, null=True)
    qualifying_start = models.CharField(max_length=16, blank=True, null=True)
    race_start = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Schedule'


class Dailyweatherforecast(models.Model):
    track_id_day = models.CharField(primary_key=True, max_length=5)
    track = models.ForeignKey('events.Track', models.DO_NOTHING)
    day = models.CharField(max_length=2)
    date = models.CharField(max_length=16, blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    precipitation = models.DecimalField(max_digits=65535, decimal_places=65535,
                                        blank=True, null=True)
    chance_of_rain = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DailyWeatherForecast'


class Hourlyweatherforecast(models.Model):
    track_id_time_slot = models.IntegerField(primary_key=True)
    track_id = models.IntegerField()
    time_slot = models.CharField(max_length=2)
    date = models.CharField(max_length=16, blank=True, null=True)
    time = models.CharField(max_length=16, blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    precipitation = models.DecimalField(max_digits=65535, decimal_places=65535,
                                        blank=True, null=True)
    chance_of_rain = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HourlyWeatherForecast'
