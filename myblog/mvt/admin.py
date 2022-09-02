from django.contrib import admin
from .models import posts
# Register your models here.
@admin.register(posts)
class grocreyAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','author','body','publish','created','updated','status']
