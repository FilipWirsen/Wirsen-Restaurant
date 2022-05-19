from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import MakeReservationForm
from django.contrib.auth.models import User
from .models import Reservation

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def reserve_table(request):

    if request.method == 'POST':
        form = MakeReservationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return render(request, 'home.html')
    else: 
        form = MakeReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form})