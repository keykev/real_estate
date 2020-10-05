from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username is taken')
                return redirect('/accounts/register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email is taken')
                    return redirect('/accounts/register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)

                    user.save()
                    messages.success(request,'User successfully created')
                    return redirect('/accounts/login')
        else:
            messages.error(request,'Password doesnt match.')
            return redirect('/accounts/register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Log in successfully')
            return redirect('/accounts/dashboard')
        else:
            messages.error(request,'username or password is incorrect')
            return redirect('/accounts/login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'Successfully logged out')
    return redirect('/accounts/login')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {'user_contacts': user_contacts}
    return render(request,'accounts/dashboard.html',context)
