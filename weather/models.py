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
