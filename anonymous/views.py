import json

from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import Anonymous, Post, Chat, Messages, Comments, PostInteraction, User, CommentInteraction
from .forms import RegisterForm, NewPost
from .helper_functions import generate_code_user, get_messages

@login_required(login_url="login/")
def index(request):
    if request.method == 'POST':
        user = request.user
        # Consume ajax request
        ajax_response = json.load(request)
        value = ajax_response['value']
        interaction = ajax_response['interaction']
        post_id = ajax_response['id']

        # Query block
        post = Post.objects.filter(id = post_id)
        get_post = Post.objects.get(id = post_id)
        get_post_interactions = PostInteraction.objects.filter(post = get_post, user = user)

        # Register like or dislike
        if interaction == 'dislike':
            dislikes = post[0].dislikes
            if interaction == 'dislike' and value < 0:
                if get_post_interactions:
                    post.update(dislikes = dislikes - 1)
                    get_post_interactions.delete()
            else:
                post.update(dislikes = dislikes + 1)
                PostInteraction.objects.create(post = get_post, user = user, dislikes = 1)
        else:
            likes = post[0].likes
            if interaction == 'like' and value < 0:
                post.update(likes = likes - 1)
                if get_post_interactions:
                    get_post_interactions.delete()
            else:
                post.update(likes = likes + 1)
                PostInteraction.objects.create(post = get_post, user = user, likes = 1)

    get_all_posts = Post.objects.all().order_by('-date')
    context = {'get_all_posts':get_all_posts}

    return render(request, 'anonymous/index.html', context)

# Chat block
@login_required(login_url="login/")
def room(request, room_name):
    # Get room with user "text publisher functionality"
    room = Chat.objects.filter(room_name = room_name)[0]
    if (room.user_sender_request == room.user_receiver_request):
        messages.error(request,"You can't text yourself")
        return redirect("/")
    chat_messages = get_messages(room_name)
    return render(request, 'anonymous/chatroom.html', {'room_name':room_name, 'messages': chat_messages})


@login_required(login_url="login/")
def new_room(request, sender, post_user):
    # Get user that wants to send message to the publisher and get Publisher
    get_sender = Anonymous.objects.get(code = sender)
    get_post_admin = Anonymous.objects.get(code = post_user)
    
    if (get_sender == get_post_admin):
        messages.error(request,"You can't text yourself!")
        return redirect("/")
    
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
        chat_messages = get_messages(room_name)
        return render(request, 'anonymous/chatroom.html', {'room_name':room_name, 'messages':chat_messages})

    else:
        number_of_rooms = Chat.objects.all().count()
        room_name = f'Anonymous{number_of_rooms}'
        Chat.objects.create(room_name = room_name, room_code = generate_room_code, user_sender_request = get_sender, user_receiver_request = get_post_admin)
        return render(request, 'anonymous/chatroom.html', {'room_name':room_name})
   
@login_required(login_url="login/")
def chat(request):
    # Display all current chats
    anonymous = Anonymous.objects.get(user = request.user)
    
    if request.method == 'POST':
        # Consume Ajax request
        ajax_response = json.load(request)
        value = ajax_response['data']
        id = ajax_response['id']
        Chat.objects.filter(id = id).update(room_name = value)

    room_list = Chat.objects.filter(Q(user_sender_request = anonymous) | Q(user_receiver_request = anonymous))
    number_of_rooms = room_list.count()
    context = {'room_list': room_list, 'number_of_rooms':number_of_rooms}
    
    return render(request, 'anonymous/chat.html', context)

# Post block
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

def comment_like(request):
    # Consume Ajax request
    if is_ajax(request=request):
        print('da')
    ajax_response = json.load(request)
    value = ajax_response['value']
    interaction = ajax_response['interaction']
    
    comment_id = ajax_response['id']

    user = request.user 
    comment = Comments.objects.filter(id = comment_id)
    get_comment = Comments.objects.get(id = comment_id)
    get_comment_interactions = CommentInteraction.objects.filter(comment = get_comment, user = user)

    # Register like or dislike
    if interaction == 'dislike':
        dislikes = comment[0].dislikes
        if interaction == 'dislike' and value < 0:
            if get_comment_interactions:
                comment.update(dislikes = dislikes - 1)
                get_comment_interactions.delete()
        else:
            comment.update(dislikes = dislikes + 1)
            CommentInteraction.objects.create(comment = get_comment, user = user, dislikes = 1)
    else:
        likes = comment[0].likes
        if interaction == 'like' and value < 0:
            comment.update(likes = likes - 1)
            if get_comment_interactions:
                get_comment_interactions.delete()
        else:
            print('taj')
            comment.update(likes = likes + 1)
            CommentInteraction.objects.create(comment = get_comment, user = user, likes = 1)


def post(request, pk):
    user_code = generate_code_user(request)
    post = Post.objects.filter(id = pk)
    post.update(views = post[0].views + 1)

    if request.method == 'POST':
        print(request)
        try:
            
            get_all_comments = comment_like(request)
            
        except:
            print('da')
            commentator = request.user
            comment = request.POST.get('comment')
            Comments.objects.create(commentator = commentator, comment = comment, post = post[0])
            return HttpResponseRedirect(f"/post/{pk}")

    # At the end so newly posted comments are queried also
    get_all_comments = Comments.objects.filter(post = post[0]).order_by('-date')
    for i in get_all_comments:
        for l in i.interaction.all():
            print(l.user == request.user)
    number_of_comments = get_all_comments.count()
    context = {'post': post[0], 'user_code': user_code, 'number_of_comments': number_of_comments, 'get_all_comments': get_all_comments}
    return render(request, 'anonymous/post.html', context)


# Authentication block
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "You are logged in successfully!")

            return redirect("/")
        else:
            messages.error(request, "Incorrect username or password. Please try again.")
            return render(request, 'anonymous/login.html')
    return render(request, 'anonymous/login.html')
    

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)   
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            generate_code = generate_code_user(request)
            try:
                Anonymous.objects.create(user = user, code = generate_code)
            except:
                pass
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "anonymous/register.html", {"form":form})


def logout_view(request):
    logout(request)
    return render(request, 'anonymous/logout.html')
    

def user_settings(request):
    get_anonymous = Anonymous.objects.get(user = request.user)
    blog_history = Post.objects.filter(user = get_anonymous).order_by('-date')
    date_joined = (request.user.date_joined).strftime('%Y-%m-%d')
    if request.method == 'POST':
        get_anonymous.delete()
        User.objects.get(username = request.user.username).delete()
        logout_view(request)

    context = {
        "blog_history": blog_history,
        "date_joined": date_joined,
    }
    return render(request, 'anonymous/user_settings.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Ajax functions

    




def delete_chat(request):
    ajax_response = json.load(request)
    id = ajax_response['id']
    if (ajax_response['action'] == 'Delete Chat'):
        del_chat = Chat.objects.filter(id = id)
        del_messages = Messages.objects.filter(room_name = del_chat[0].room_name)
        del_chat.delete()
        del_messages.delete()
        
    return HttpResponseRedirect("/chat/")