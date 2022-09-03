from django.contrib import admin
from .models import posts,comments,contact
# Register your models here.
@admin.register(posts)
class postsAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','author','body','publish','created','updated','status']


@admin.register(comments)
class commentsADMIN(admin.ModelAdmin):
    list_display = ['id','name','email','comment','post']


@admin.register(contact)
class contactADMIN(admin.ModelAdmin):
    list_display = ['id','name','email']