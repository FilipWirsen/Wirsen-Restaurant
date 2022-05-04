from django.contrib import admin
from .models import Table, Customer, Reservation

# Register your models here.

admin.site.register(Table)
admin.site.register(Customer)
admin.site.register(Reservation)
