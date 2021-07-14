from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contacts

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('accounts:register')
            else :
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already registered ')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                               last_name=last_name, email=email)
                    user.save()
                    messages.success(request, 'You are successfully registered')
                    return redirect('accounts:login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')



    else:
        return render(request, "accounts/register.html")

def login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password= password)

        if user is not None :
            auth.login(request , user)
            messages.success(request, 'You are succesfully logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'User does not exist')
            return redirect('accounts:login')

    else:
       return render(request, "accounts/login.html")

def logout(request):
      messages.success(request, 'You have successfully logged out')
      auth.logout(request)
      return redirect('pages:index')

def dashboard(request):
    contacts = Contacts.objects.filter(user_id=request.user.id)
    contt={'contacts' : contacts}
    return render(request, "accounts/dashboard.html", contt)