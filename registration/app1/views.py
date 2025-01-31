from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app1.models import CustomUser  # Import CustomUser model


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1 != pass2:
            messages.error(request, f"Your Password & Confirm Password Are Not Same!!!")
            return redirect('signup')
            # return HttpResponse("Your Password & Confirm Password Are Not Same!!!")
        else:            
            my_user=CustomUser.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        #return HttpResponse("User has been created sucessfully!!!")
        
        print(uname,email,pass1,pass2)
    return render(request,'signup.html')
    

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(f"username : {username} \npassword : {pass1}")
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Add an error message to display in the pop-up
            messages.error(request, f"Username or Password is Incorrect!")
            # return render(request, 'login.html')
    
    return render(request, 'login.html')

def LogoutPage(request):
        logout(request)
        return redirect('login')
       




