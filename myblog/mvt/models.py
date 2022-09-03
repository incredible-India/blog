from datetime import datetime 
from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class posts(models.Model):
    STATUS_CHOICES	=	(('draft',	'Draft'),('published',	'Published'),)
    title =	models.CharField(max_length=300)
    slug	=	AutoSlugField(populate_from='title',max_length=250,unique=True,null=True,default=None) 
    author	=	models.CharField(max_length=250)
    body	=	models.TextField()
    publish	=	models.DateTimeField(default=datetime.now(), blank=True)
    created	=	models.DateTimeField(auto_now_add=True)
    updated	=	models.DateTimeField(auto_now=True)
    status	=	models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')



class comments(models.Model):
    post = models.ForeignKey(posts,on_delete=models.CASCADE)
    name =  models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    comment = models.TextField()


class contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)