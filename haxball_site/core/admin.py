from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)
    list_filter = ('created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created')

@admin.register(LikeDislike)
class LikeDisLike(admin.ModelAdmin):
    list_display = ('vote', 'user', 'content_type', 'object_id', 'content_object')