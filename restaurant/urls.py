from django.urls import path
from . import views
from .views import ReservationView

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation', views.reservation, name='reservation'),
]
