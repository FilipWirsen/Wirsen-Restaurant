# Generated by Django 3.2.13 on 2022-05-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_reservation_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='book_time',
            field=models.IntegerField(choices=[(1, '17:30'), (2, '17:45'), (3, '18:00'), (4, '18:15'), (5, '18:30'), (6, '18:45'), (7, '19:00'), (8, '19:15'), (9, '19:30'), (10, '19:45'), (11, '20:00'), (12, '20:15'), (13, '20:30'), (14, '20:45'), (15, '21:00'), (16, '21:15'), (17, '21:30'), (18, '21:45'), (19, '22:00')]),
        ),
    ]
