# Generated by Django 3.0.8 on 2020-09-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeekSchedule', '0004_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.TextField(choices=[('1', 'Done'), ('2', '1/3 left'), ('3', 'Just started'), ('4', 'Failed'), ('5', 'Waiting')], default='5'),
        ),
    ]
