
from django.urls import path,include
from . import views
urlpatterns = [
  
    path('',views.index,name='homepage'),
    path('post/',views.Mypost.as_view(),name='myposts')
]
