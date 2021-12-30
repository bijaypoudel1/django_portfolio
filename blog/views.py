from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from blog.models import Post,Comment

# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,'blog/blog.html', {"page": "blog","post":post})


def blog_single(request,slug):
   q = Post.objects.filter(slug__iexact = slug)
   if q.exists():
      q = q.first()
   else:
      return HttpResponse('<h1>Post Not Found</h1>')
   context = {
      "page": "blog",
      'post': q
   }
   # post = Post.objects.order_by('slug')

   return render(request,'blog/blog-single.html', context)


def comment(request,slug):
   if request.method=="POST":
      name = request.POST['name']
      email = request.POST['email']
      website = request.POST['website']
      message = request.POST['message']
      fm = Comment(name=name,email=email,website=website,message=message)
      fm.save()
      q = Post.objects.filter(slug__iexact = slug)
      if q.exists():
         q = q.first()
      else:
         return HttpResponse('<h1>Post Not Found</h1>')
      context = {
      "page": "blog",
      'post': q
      }
      return render(request,'blog/blog-single.html', context)
   else:
      return HttpResponse('<h1>Post Not Found</h1>')









