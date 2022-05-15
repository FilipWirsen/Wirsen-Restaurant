from django.urls import path
from .views import UserRegisterView, EditUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', EditUserView.as_view(), name='profile'),
]
