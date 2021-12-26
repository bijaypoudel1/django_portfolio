from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main/index.html', {"page": "home"})

def about(request):
    return render(request,'main/about.html', {"page": "about"})

def work(request):
    return render(request,'main/work.html', {"page": "work"})

def blog(request):
    return render(request,'main/blog.html', {"page": "blog"})

def blog_single(request):
    return render(request,'main/blog-single.html', {"page": "blog"})

def contact(request):
    return render(request,'main/contact.html', {"page": "contact"})