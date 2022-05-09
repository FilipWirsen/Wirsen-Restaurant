from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created')
            return render(request, 'index.html')
    else:
        form = SignUpForm()

    args = {}
    args['form'] = form
    return render(request, 'signup.html', args)

    # user = request.user
    # profile = user.profile
    #if we have a user that has already selected info, it will pass in this info