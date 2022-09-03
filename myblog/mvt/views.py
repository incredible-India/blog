import email
from inspect import trace
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import posts as pts
from .models import comments as cmt
from .models import contact as ct
from django.views import View
from django.views.generic.list import ListView
from django.contrib import messages
from	django.core.mail	import	send_mail

# Create your views here.
def index(request):
    if request.method == 'GET':
        mypts = pts.objects.all().order_by('created')[:3]
        #only three post will be at the index page for all posts we make extra page fir the posts
        return render(request, 'mvt/index.html',{
            'posts' : mypts
        })

    #if someone try to contact
    if request.method == 'POST':
        name = request.POST.get('name')
        email=request.POST.get('email')

        savecnt = ct.objects.create(name=name, email=email)

        messages.info(request,"Your info has been recorded, soon our team will try to contact you..")

        return HttpResponseRedirect('/')








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
            
            pos = pts.objects.get(slug=data)

            mycmt = cmt.objects.filter(post=pos)
            return render(request,'mvt/comment.html',{'pts':mypts
            
            ,'cmt' : mycmt
            })
        else:
            return HttpResponse('<h1> SomeThing Went Worng ooops! </h1>')

        
    #if some comment and submit the form
    def post(self,request,data):
        

        mypts = pts.objects.filter(slug=data)

        if(len(mypts) == 1):

            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')

            savecmnt = cmt.objects.create(name = name,email = email,comment = comment,post = pts.objects.get(slug=data))
            
            return HttpResponseRedirect(f'/spcl/{data}')
        else:
            return HttpResponse('<h1> Something went worng</h1>')





def share_post(request, postID):
    post	=	get_object_or_404(pts,id=postID)
    sent=False
    message = False
    if	request.method	==	'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        comment = request.POST.get('comment')
        tosend = request.POST.get('tosend')
        
        if tosend==email:
            message='Sender And Receiver Email Cannot Be Same'
        else:
            post_url	=	request.build_absolute_uri()#post.get_absolute_url()
            print(post_url)
            subject	=	f'{name}	({email})	recommends	you	reading	"{post.title}"'
            msg	= f'Read	"{post.title}"	at	{post_url}\n\n{name}\'s	comments:	{comment}'
            send_mail(subject,	msg,email,[tosend])
            sent=True
            message = f'Post Sent successfully to {tosend}'
    
    
    return render(request,'mvt/sharepost.html',
        {
            'post': post,
            'status': sent,
            'message' : message
        })




