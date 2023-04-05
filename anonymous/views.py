from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'anonymous/index.html')

def room(request, room_name):
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name})

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'anonymous/index.html')
        else:
            pass # dispaly message
    return render(request, 'anonymous/login.html')
