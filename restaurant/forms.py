from django.forms import ModelForm
from .models import Reservation
from django import forms


class MakeReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('party_size', 'book_date', 'book_time')


class ReservationForm(forms.ModelForm):
    table = forms.IntegerField()
    class Meta:
        model = Reservation
        fields = ['user', 'table', 'book_date', 'book_time']
        widgets = {
            'user': forms.HiddenInput(),
        }