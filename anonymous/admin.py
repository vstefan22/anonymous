from django.contrib import admin
from .models import Anonymous, Post, Chat, Messages, Comments, PostInteraction, CommentInteraction
admin.site.register(Anonymous)
admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Messages)
admin.site.register(Comments)
admin.site.register(PostInteraction)
admin.site.register(CommentInteraction)