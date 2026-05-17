from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from rest_framework import generics, permissions

from .forms import SignUpForm
from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


def signup_page(request):
    if request.user.is_authenticated:
        return redirect('event-list-page')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created. Welcome in.')
            return redirect('event-list-page')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


def logout_page(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('event-list-page')
