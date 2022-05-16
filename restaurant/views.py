from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import ReservationForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class ReservationView(generic.CreateView):

    form_class = ReservationForm
    template_name = 'reservation/reservation.html'
    success_url = reverse_lazy('home')


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.hmtl')
        return render(request, 'reservation/reservation.html', {'form': form})
    else:
        default_data = {'user': User.objects.get(pk=request.user.pk)}
        form = ReservationForm(default_data)
        return render(request, 'reservation/reservation.html', {'form': form})
