from django.forms import ModelForm
from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    table = forms.IntegerField()
    class Meta:
        model = Reservation
        fields = ['user', 'table', 'book_date', 'book_time']
        widgets = {
            'user': forms.HiddenInput(),
        }