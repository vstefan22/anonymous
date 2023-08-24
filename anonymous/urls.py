from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('chat/<str:room_name>/', views.room, name = 'room'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout_view, name = 'logout'),
    path('new-post/', views.new_post, name = 'new_post'),
    path('new-room/<str:sender>/<str:post_user>/', views.new_room, name = 'new_room'),
    path('chat/', views.chat, name = 'chat'),
    path('post/<int:pk>/', views.post, name = 'post'),
    path('comment-like/<int:pk>/<int:post_id>/', views.comment_like, name = 'comment-like'),
    path('delete-chat/', views.delete_chat, name = 'delete_chat'),
    path('user-settings/', views.user_settings, name = 'user_settings')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)