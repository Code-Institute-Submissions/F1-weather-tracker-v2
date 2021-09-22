# Generated by Django 3.2.7 on 2021-09-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dailyweatherforecast',
            fields=[
                ('track_id_day', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=2)),
                ('date', models.CharField(blank=True, max_length=16, null=True)),
                ('min_temp', models.IntegerField(blank=True, null=True)),
                ('max_temp', models.IntegerField(blank=True, null=True)),
                ('precipitation', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('chance_of_rain', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DailyWeatherForecast',
                'managed': False,
            },
        ),
    ]