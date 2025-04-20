from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomLoginForm

def home(request):
    users = CustomUser.objects.all()  # Fetch all users from database
    user_count = users.count()        # Total number of registered users

    return render(request, 'home.html', {
        'users': users,
        'user_count': user_count
    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created.")
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
