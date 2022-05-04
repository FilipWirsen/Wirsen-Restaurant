from django.db import models

# Create your models here.


class Table(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.capacity}"


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Reservation(models.Model):
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5)
    party_size = models.IntegerField()
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"Date:{self.date}, Time:{self.time}, Table Number{self.table_id}"


