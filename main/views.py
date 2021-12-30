from django.shortcuts import render
from .models import Work, ExpertTeam, Client
from blog.models import Post
# Create your views here.

def home(request):
    wd = Work.objects.all()
    cd = Client.objects.all()
    post = Post.objects.order_by('-time')
    return render(request,'main/index.html', {"page": "home", "work":wd , "client":cd, "post":post})

def about(request):
    cd = Client.objects.all()
    expertData = ExpertTeam.objects.all()
    return render(request,'main/about.html', {"page": "about", "ed":expertData,"client":cd })

def work(request):
    wd = Work.objects.all()
    return render(request,'main/work.html', {"page": "work",'wd':wd})


def contact(request):
    return render(request,'main/contact.html', {"page": "contact"})


    