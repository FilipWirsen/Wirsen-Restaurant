# Generated by Django 3.2.13 on 2022-05-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_siteuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='full_name',
            field=models.CharField(default=True, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]