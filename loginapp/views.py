# from  import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
    # return HttpResponse("hello i'm working")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

    # now validation here 
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist,please try some other username")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists!')
            return redirect('signup')
        if len(username)>10:
            messages.error(request,'username must be 10 characters')
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,'username must be Alpha-Numeric!')
            return redirect('signup')
        if pass1!=pass2:
            messages.error(request,"Password didn't match!")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Account has been successfully created.")
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        pass1=request.POST.get('pass1')
        # pass2=request.POST.get('pass2')

        user=authenticate(username=username,password=pass1)
        # if pass1!=pass2:
        #     messages.error(request,"Password didn't match! ")
        #     return redirect('home')

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"home.html",{'fname':fname})
        else:
            messages.error(request,"Bad Crediential")
            return redirect('signin')
    return render(request,'signin.html')


def signout(request):
    logout(request)
    messages.success(request,"Logout successfully !")
    return redirect('home')