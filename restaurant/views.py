from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .forms import MakeReservationForm
from django.contrib.auth.models import User
from .models import Reservation, Table
from django.views import generic, View
from django.template import RequestContext
from .availability import CheckAvailability

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
            post.end_time = post.time + 8
            get_date = Reservation.objects.filter(book_date=post.date)
            get_relevant_bookings = get_date.filter(book_time__range=(post.time, post.end_time))
            number_of_bookings_before = get_relevant_bookings.count()
            if post.size <= 2:
                if number_of_bookings_before >= 5:
                    return HttpResponse("Time not avaibile xd")
                elif number_of_bookings_before < 5:
                    table = Table.objects.filter(table_size=2).first()
                    post.table = table
                    post.save()
                    return HttpResponse("Booked")

            #if post.size <= 2:
             #   table = Table.objects.filter(table_size=2).first()
              #  post.table = table
            #elif post.size >= 3:
             #   table = Table.objects.filter(table_size=4).first()
              #  post.table = table
                
            #check_date = Reservation.objects.filter(book_date=post.date)
            #check_time = check_date.filter(book_time=post.time)
            #if check_time.exists():
             #   return HttpResponse("Time not availible")
            #else:
             #   post.save()
              #  return render(request, 'home.html')
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



