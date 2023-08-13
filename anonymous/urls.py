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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)