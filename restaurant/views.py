from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .forms import MakeReservationForm
from django.contrib.auth.models import User
from .models import Reservation, Table
from django.views import generic, View
from django.template import RequestContext
from .availability import CheckAvailability
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def reserve_table(request):
    
    if request.method == 'POST':
        form = MakeReservationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            data = form.cleaned_data
            post.size = data['party_size']
            post.date = data['book_date']
            post.time = data['book_time']
            time = int(data['book_time'])
            post.end_time = time + 8
            get_date = Reservation.objects.filter(book_date=post.date)
            bookings_before = time - 7
            bookings_after = time + 7
            get_bookings_before = get_date.filter(
                book_time__range=(bookings_before, time))
            get_bookings_after = get_date.filter(
                book_time__range=(time, bookings_after))
            if post.size <= 2:
                if get_bookings_before.count() >= 5 or get_bookings_after.count() >= 5 and get_bookings_after.count() + get_bookings_before.count() <= 9:
                    messages.error(request, 'Time not avalible')
                    form = MakeReservationForm()
                    return render(request, 'reservation/reservation.html', {'form': form})
                else:
                    tables = Table.objects.filter(table_size=2)
                    for table in tables:
                        if not Reservation.objects.filter(book_date=post.date, book_time__range=(get_bookings_after.count(), get_bookings_before.count()), table=table).exists():
                            post.table = table
                        else: 
                            HttpResponse("Error")
                    form = MakeReservationForm()
                    post.save()
                    messages.success(request, 'Booked')
                    return render(request, 'reservation/reservation.html', {'form': form})

            elif post.size >= 4:
                if get_bookings_before.count() >= 5 or get_bookings_after.count() >= 5 and get_bookings_after.count() + get_bookings_before.count() <= 9:
                    return HttpResponse("Time not avaibile xd")
                else:
                    tables = Table.objects.filter(table_size=4)
                    for table in tables:
                        if not Reservation.objects.filter(book_date=post.date, book_time__range=(get_bookings_before.count(), get_bookings_after.count()), table=table).exists():
                            post.table = table
                    post.save()
                    return HttpResponse(f"Booked Bookings before: {get_bookings_before.count()} Bookings After: {get_bookings_after.count()} Time: {time}")
    else: 
        form = MakeReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form})


class ReservationDetail(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        reservations = Reservation.objects.filter(user=user)
        return render(
            request,
            'reservation/edit_reservation.html',
            {
                'reservations': reservations
            })



