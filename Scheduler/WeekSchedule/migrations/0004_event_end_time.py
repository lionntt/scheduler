# Generated by Django 3.0.8 on 2020-09-20 07:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WeekSchedule', '0003_auto_20200912_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 7, 44, 26, 22025, tzinfo=utc)),
            preserve_default=False,
        ),
    ]