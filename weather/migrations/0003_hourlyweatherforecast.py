# Generated by Django 3.2.7 on 2021-09-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_dailyweatherforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hourlyweatherforecast',
            fields=[
                ('track_id_time_slot', models.IntegerField(primary_key=True, serialize=False)),
                ('track_id', models.IntegerField()),
                ('time_slot', models.CharField(max_length=2)),
                ('date', models.CharField(blank=True, max_length=16, null=True)),
                ('time', models.CharField(blank=True, max_length=16, null=True)),
                ('temperature', models.IntegerField(blank=True, null=True)),
                ('precipitation', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('chance_of_rain', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'HourlyWeatherForecast',
                'managed': False,
            },
        ),
    ]