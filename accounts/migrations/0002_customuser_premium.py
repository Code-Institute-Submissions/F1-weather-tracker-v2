# Generated by Django 3.2.7 on 2021-09-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
