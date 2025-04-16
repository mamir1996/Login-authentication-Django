# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from .models import CustomUser  # using your custom user model

# # Create your views here.

# def home(request):
#     users = CustomUser.objects.all()  # Fetch all users from database
#     user_count = users.count()        # Total number of registered users

#     return render(request, 'home.html', {
#         'users': users,
#         'user_count': user_count
#     })



# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
#         phone = request.POST.get('phone')

#         # Validation
#         if CustomUser.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists, please try another one.")
#             return redirect('signup')

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists!')
#             return redirect('signup')

#         if len(username) > 10:
#             messages.error(request, 'Username must be under 10 characters.')
#             return redirect('signup')

#         if not username.isalnum():
#             messages.error(request, 'Username must be Alpha-Numeric!')
#             return redirect('signup')

#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match!")
#             return redirect('signup')

#         # Create the user using CustomUser model
#         myuser = CustomUser.objects.create_user(
#             username=username,
#             email=email,
#             password=pass1,
#             phone_number=phone
#         )
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()

#         messages.success(request, "Your account has been successfully created.")
#         return redirect('signin')

#     return render(request, 'signup.html')


# def signin(request):
#     if request.method == "POST":
#         username = request.POST.get('uname')
#         pass1 = request.POST.get('pass1')

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return render(request, "home.html", {'fname': fname})
#         else:
#             messages.error(request, "Invalid credentials.")
#             return redirect('signin')

#     return render(request, 'signin.html')


# def signout(request):
#     logout(request)
#     messages.success(request, "Logged out successfully!")
#     return redirect('home')





from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomLoginForm

def home(request):
    return render(request, 'home.html')


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
