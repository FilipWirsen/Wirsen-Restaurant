from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from .models import SiteUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            email = form.cleaned_data.get('email')
            SiteUser.objects.create(user=user, email=email)
            login(request, user)
            messages.success(request, 'Account Created')
            return render(request, 'index.html')
    else:
        form = SignUpForm()

    args = {}
    args['form'] = form
    return render(request, 'signup.html', args)


def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, 'signup.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html')