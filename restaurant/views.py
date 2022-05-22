from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .forms import MakeReservationForm
from django.contrib.auth.models import User
from .models import Reservation, Table
from django.views import generic, View

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
            if Reservation.objects.filter(user=post.user).exists():
                return HttpResponse('You already have a reservation, You can edit or cancel it under "Manage Reservation"')
            elif Reservation.objects.filter(book_date=post.date).exists() and Reservation.objects.filter(book_time=post.time).exists():
                return HttpResponse("Time not availible")
            elif post.size <= 2:
                Table.objects.filter(booked=False)
            else:
                post.save()
                return render(request, 'home.html')
    else: 
        form = MakeReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form})


class ReservationDetail(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        queryset = Reservation.objects.filter(user=user)
        reservation = get_object_or_404(queryset)
        return render(
            request,
            'reservation/edit_reservation.html',
            {
                'reservation': reservation
            })