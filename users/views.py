from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created, please log in.")
            return redirect('home')
    else: 
        form = forms.UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

