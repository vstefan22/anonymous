from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Anonymous, Post
from .forms import RegisterForm, NewPost
import shortuuid


# Create your views here.

def index(request):
    id = shortuuid.ShortUUID().random(length=6)
    get_all_posts = Post.objects.all()
    context = {'get_all_posts':get_all_posts}

    return render(request, 'anonymous/index.html', context)

@login_required
def room(request, room_name):
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name})

@login_required
def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewPost(request.POST)
            if form.is_valid():
                title =  form.cleaned_data["title"]
                description =  form.cleaned_data["description"]
                user = request.user
                Post.objects.create(title = title, description = description, user = user)
        form = NewPost()
        context = {'form':form}
        return render(request, 'anonymous/new_post.html', context)
    else:
       return render(request, 'anonymous/login.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,"You are logged in successfully!")
            context = {'green':'green'}
            return render(request, 'anonymous/index.html', context)
        else:
            messages.error(request,"Incorrect username or password. Please try again.")
            return render(request, 'anonymous/login.html')
    return render(request, 'anonymous/login.html')
    

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "anonymous/register.html", {"form":form})

def logout_view(request):
    logout(request)
    return render(request, 'anonymous/logout.html')