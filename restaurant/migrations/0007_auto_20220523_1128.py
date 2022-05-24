# Generated by Django 3.2.13 on 2022-05-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20220522_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='book_time',
            field=models.CharField(choices=[('17:30', '17:30'), ('17:45', '17:45'), ('18:00', '18:00'), ('18:15', '18:15'), ('18:30', '18:30'), ('18:45', '18:45'), ('19:00', '19:00'), ('19:15', '19:15'), ('19:30', '19:30'), ('19:45', '19:45'), ('20:00', '20:00'), ('20:15', '20:15'), ('20:30', '20:30'), ('20:45', '20:45'), ('21:00', '21:00'), ('21:15', '21:15'), ('21:30', '21:30'), ('21:45', '21:45'), ('22:00', '22:00')], max_length=5),
        ),
    ]
