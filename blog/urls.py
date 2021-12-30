from django.urls import path
from . import views

urlpatterns = [
     path('blog/', views.blog,name="blog"),
    path('blog/<slug>', views.blog_single,name="blog_single"),
    path('comment/<slug>',views.comment, name="comment")
]

