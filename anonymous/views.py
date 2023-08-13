from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Anonymous, Post, Chat, Messages, Comments
from .forms import RegisterForm, NewPost
from django.db.models import Q
import shortuuid
import json
from django.http import HttpResponseRedirect

def generate_code_user(request):
    id = shortuuid.ShortUUID().random(length=6)
    try:
        user_acc = Anonymous.objects.filter(user = request.user)
    except:
        user_acc = Anonymous.objects.create(user = request.user, code = id)
        return user_acc.code
    if user_acc:
        if user_acc[0].code:
            pass
        else:
             user_acc = Anonymous.objects.filter(user = request.user).create(code = id)
    else:
        user_acc = Anonymous.objects.create(user = request.user, code = id)
        return user_acc.code
    return user_acc[0].code

def get_messages(request, room_name):
    get_messages = Messages.objects.filter(room_name = room_name).order_by('date_time')
    pass_json = {'message':[]}

    for message in get_messages:
        pass_json['message'].append(message.message)
        
    messages = json.dumps(pass_json)
    return messages
@login_required(login_url="login/")

def index(request):
    if request.method == 'POST':
        ajax_response = json.load(request)
        value = ajax_response['value']
        interaction = ajax_response['interaction']
        post_id = ajax_response['id']
        post = Post.objects.filter(id = post_id)
        dislikes = post[0].dislikes
        likes = post[0].likes
        
        if interaction == 'd':
            if interaction == 'd' and value < 0:
                post.update(dislikes = dislikes - 1)
            else:
                post.update(dislikes = dislikes + 1)
        else:
            if interaction == 'l' and value < 0:
                post.update(likes = likes - 1)
            else:
                post.update(likes = likes + 1)

        
    
    get_all_posts = Post.objects.all().order_by('-date')
    context = {'get_all_posts':get_all_posts}

    return render(request, 'anonymous/index.html', context)

@login_required(login_url="login/")
def room(request, room_name):
    messages = get_messages(request, room_name)
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name, 'messages':messages})

@login_required(login_url="login/")
def new_room(request, sender, post_user):
    # Get user that wants to send message to the publisher and get Publisher
    get_sender = Anonymous.objects.get(code = sender)
    get_post_admin = Anonymous.objects.get(code = post_user)

    # Get UUID from both users
    get_sender_code = get_sender.code
    get_post_admin_code = get_post_admin.code

    # Create Unique code for room 
    generate_room_code = get_sender_code + get_post_admin_code
    check_for_reverse_room = get_post_admin_code + get_sender_code
    # Check for duplicate rooms

    check_room = Chat.objects.filter(Q(room_code = generate_room_code) | Q(room_code = check_for_reverse_room))
    
    if check_room:
        room_name = check_room[0].room_name
        messages = get_messages(request, room_name)
        return render(request, 'anonymous/chatroom.html', {'room_name':room_name, 'messages':messages})

    else:
        number_of_rooms = Chat.objects.all().count()
        room_name = f'Anonymous{number_of_rooms}'
        Chat.objects.create(room_name = room_name, room_code = generate_room_code, user_sender_request = get_sender, user_receiver_request = get_post_admin)
        return render(request, 'anonymous/chatroom.html', {'room_name':room_name})
   
@login_required(login_url="login/")
def chat(request):
    anonymous = Anonymous.objects.get(user = request.user)
    room_list = Chat.objects.filter(Q(user_sender_request = anonymous) | Q(user_receiver_request = anonymous))
    number_of_rooms = len(room_list)
    
    context = {'room_list': room_list, 'number_of_rooms':number_of_rooms}
    
    return render(request, 'anonymous/chat.html', context)

@login_required(login_url="login/")
def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewPost(request.POST)
            if form.is_valid():
                title =  form.cleaned_data["title"]
                description =  form.cleaned_data["description"]
                user = request.user
                anonymous = Anonymous.objects.get(user = user)
                Post.objects.create(title = title, description = description, user = anonymous)
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

            return redirect("/", context)
        else:
            messages.error(request,"Incorrect username or password. Please try again.")
            return render(request, 'anonymous/login.html')
    return render(request, 'anonymous/login.html')
    

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)   
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            print(request.user.username)
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "anonymous/register.html", {"form":form})

def logout_view(request):
    logout(request)
    return render(request, 'anonymous/logout.html')

def post(request, pk):
    user_code = generate_code_user(request)
    post = Post.objects.filter(id = pk)
    views = post[0].views
    post.update(views = views + 1)
    if request.method == 'POST':
        commentator = request.user
        comment = request.POST.get('comment')
        Comments.objects.create(commentator = commentator, comment = comment, post = post[0])
        return HttpResponseRedirect(f"/post/{pk}")

    get_comments = Comments.objects.filter(post = post[0])
    number_of_comments = Comments.objects.filter(post = post[0]).count()
    context = {'post': post[0], 'comments':get_comments, 'user_code': user_code, 'number_of_comments': number_of_comments}
    return render(request, 'anonymous/post.html', context)


def comment_like(request, pk, post_id):
    # from django.utils import simplejson
    ajax_response = json.load(request)
    value = ajax_response['value']
    interaction = ajax_response['interaction']
    comment_id = ajax_response['id']
    comment = Comments.objects.filter(id = comment_id)
    dislikes = comment[0].dislikes
    likes = comment[0].likes
    
    if interaction == 'd':
        if interaction == 'd' and value < 0:
            comment.update(dislikes = dislikes - 1)
        else:
            comment.update(dislikes = dislikes + 1)
    else:
        if interaction == 'l' and value < 0:
            comment.update(likes = likes - 1)
        else:
            comment.update(likes = likes + 1)

    
    return HttpResponseRedirect(f"/post/{post_id}")
    