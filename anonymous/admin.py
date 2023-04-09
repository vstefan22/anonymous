from django.contrib import admin
from .models import Anonymous, Post, Chat
admin.site.register(Anonymous)
admin.site.register(Post)
admin.site.register(Chat)