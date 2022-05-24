from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.user} {self.name}"


class Table(models.Model):
    TableID = models.AutoField(primary_key=True)
    table_size = models.IntegerField()

    def __str__(self):
        return f"Table Number: {self.TableID}, Table Size: {self.table_size}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    book_date = models.DateField(default=timezone.now)
    TIME_CHOICES = [
        (1, '17:30'),
        (2, '17:45'),
        (3, '18:00'),
        (4, '18:15'),
        (5, '18:30'),
        (6, '18:45'),
        (7, '19:00'),
        (8, '19:15'),
        (9, '19:30'),
        (10, '19:45'),
        (11, '20:00'),
        (12, '20:15'),
        (13, '20:30'),
        (14, '20:45'),
        (15, '21:00'),
        (16, '21:15'),
        (17, '21:30'),
        (18, '21:45'),
        (19, '22:00'),
    ]
    book_time = models.IntegerField(choices=TIME_CHOICES)
    end_time = models.IntegerField(blank=True)

