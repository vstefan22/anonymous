from django.contrib import admin
from .models import Anonymous, Post, Chat, Messages
admin.site.register(Anonymous)
admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Messages)