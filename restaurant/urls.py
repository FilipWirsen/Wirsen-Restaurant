from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('createuser', views.createUser, name='createuser'),
    path('signup', views.signup, name='signup')
]