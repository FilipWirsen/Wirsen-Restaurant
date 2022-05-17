# Generated by Django 3.2.13 on 2022-05-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20220516_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='table',
            new_name='table_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='party_size',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='book_time',
            field=models.CharField(choices=[('17:30', '17:30'), ('17:45', '17:45'), ('18:00', '18:00'), ('18:15', '18:15')], max_length=5),
        ),
    ]
