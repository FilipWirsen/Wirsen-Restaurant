from .models import Reservation, Table
from django.shortcuts import HttpResponse


def CheckAvailability(party_size, book_date, start_time, end_time):
    get_date = Reservation.objects.filter(book_date=book_date)
    get_relevant_bookings = get_date.filter(
        start_time < start_time-200)
    number_of_bookings_before = get_relevant_bookings.count()
    if party_size <= 2:
        if number_of_bookings_before >= 5:
            return HttpResponse("Time not avaibile xd")
        elif number_of_bookings_before < 5:
            return HttpResponse("Booked")
