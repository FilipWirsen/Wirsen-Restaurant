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
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.table_size}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    party_size = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    book_date = models.DateField(default=timezone.now)
    TIMES = [
        ('17:30', '17:30'),
        ('17:45', '17:45'),
        ('18:00', '18:00'),
        ('18:15', '18:15'),
    ]
    book_time = models.CharField(
        max_length=5,
        choices=TIMES,
        blank=True
    )

