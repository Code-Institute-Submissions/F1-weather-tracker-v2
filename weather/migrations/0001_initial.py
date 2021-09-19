# Generated by Django 3.2.7 on 2021-09-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('practice1_start', models.CharField(blank=True, max_length=16, null=True)),
                ('practice2_start', models.CharField(blank=True, max_length=16, null=True)),
                ('practice3_start', models.CharField(blank=True, max_length=16, null=True)),
                ('qualifying_start', models.CharField(blank=True, max_length=16, null=True)),
                ('race_start', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'Schedule',
                'managed': False,
            },
        ),
    ]