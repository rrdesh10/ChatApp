from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        userform = RegisterForm(request.POST)
        if userform.is_valid():
            new_user = userform.save(commit=False)
            new_user.set_password(userform.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        userform = RegisterForm()
        return render(request, 'users/register.html', {'userform':userform})
