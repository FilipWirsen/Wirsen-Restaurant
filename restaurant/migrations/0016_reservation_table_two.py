# Generated by Django 3.2.13 on 2022-05-28 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_alter_reservation_book_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_two', to='restaurant.table'),
        ),
    ]