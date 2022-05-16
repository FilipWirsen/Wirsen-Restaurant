# Generated by Django 3.2.13 on 2022-05-16 11:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_reservation_book_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('TableID', models.AutoField(primary_key=True, serialize=False)),
                ('table_size', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='table_size',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='book_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
            preserve_default=False,
        ),
    ]
