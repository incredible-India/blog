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





#when some will click on the all post
class Mypost(ListView):
  
    model = pts #database of post
    
    template_name = 'mvt/posts.html'
    context_object_name = 'posts'
    ordering = ['id']
    paginate_by = 4



class comment(View):
    def get(self, request,data):
        mypts = pts.objects.filter(slug=data)
        #slug will be unique and its length will always be 1 coz for each slug is different and unique
        
        if(len(mypts) == 1):
       
            return render(request,'mvt/comment.html',{'pts':mypts})
        else:
            return HttpResponse('<h1> SomeThing Went Worng ooops! </h1>')



