# Generated by Django 3.2.13 on 2022-05-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_alter_reservation_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.CharField(blank=True, choices=[('23:30', '23:30'), ('22:00', '22:00'), ('20:15', '20:15'), ('22:30', '22:30'), ('20:00', '20:00'), ('20:45', '20:45'), ('21:00', '21:00'), ('19:45', '19:45'), ('23:00', '23:00'), ('22:45', '22:45'), ('23:45', '23:45'), ('22:15', '22:15'), ('19:30', '19:30'), ('21:15', '21:15'), ('21:30', '21:30'), ('00:00', '00:00'), ('23:15', '23:15'), ('21:45', '21:45'), ('20:30', '20:30')], max_length=5),
        ),
    ]
