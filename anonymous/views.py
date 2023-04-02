from django.shortcuts import render

def index(request):
    
    return render(request, 'anonymous/index.html')

def room(request, room_name):
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name})
