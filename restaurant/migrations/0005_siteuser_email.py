# Generated by Django 3.2.13 on 2022-05-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_siteusers_siteuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='email',
            field=models.EmailField(default=True, max_length=25, unique=True),
            preserve_default=False,
        ),
    ]