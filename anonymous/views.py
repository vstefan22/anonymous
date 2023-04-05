from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import shortuuid
from .models import ID, Anonymous
# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

def index(request):
    id = shortuuid.ShortUUID().random(length=6)
    print(id)
    return render(request, 'anonymous/index.html')

def room(request, room_name):
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name})

def login(request):
    if request.method == 'POST':
        username = "Anonymous"
        get_user_number = Anonymous.objects.filter(user = request.user)[0].user_number
        generate_username = f'{username}{get_user_number}'
        password = request.POST["password"]
        user = authenticate(request, username=generate_username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'anonymous/index.html')
        else:
            pass # dispaly message
    return render(request, 'anonymous/login.html')

def register(response):
    form = RegisterForm()
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(form)
        #if form.is_valid():
            #form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "anonymous/register.html", {"form":form})