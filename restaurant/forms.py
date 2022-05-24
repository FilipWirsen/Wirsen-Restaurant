from django.forms import ModelForm
from .models import Reservation
from django import forms


class MakeReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('party_size', 'book_date', 'book_time')
        exclude = ('table', 'end_time')