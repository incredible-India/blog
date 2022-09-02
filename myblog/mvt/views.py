from django.shortcuts import render
from django.http import HttpResponse
from .models import posts as pts
from django.views import View
from django.views.generic.list import ListView
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    if request.method == 'GET':
        mypts = pts.objects.all().order_by('created')[:3]
        #only three post will be at the index page for all posts we make extra page fir the posts
        return render(request, 'mvt/index.html',{
            'posts' : mypts
        })






class Mypost(ListView):
  
    model = pts #database of post
    
    template_name = 'mvt/posts.html'
    context_object_name = 'posts'
    ordering = ['id']
    paginate_by = 4



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["userdata"] =  self.request.userdata
    #     return context

