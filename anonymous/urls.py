from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('login/', views.login, name = 'login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)