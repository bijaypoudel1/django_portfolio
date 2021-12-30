from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.template.defaultfilters import safe, truncatewords
from django.db.models.signals import pre_save
from django.dispatch import receiver

from portfolio.utils import unique_slug_generator






# Create your models here.

class Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    

class Post(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20, default='Admin')
    time = models.DateTimeField(auto_now_add=True )
    image = models.ImageField(upload_to='media/')
    content = RichTextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    


    @property
    def short_content(self):
        return truncatewords(self.content, 10)

    def thumbnail(self):
        return mark_safe('<img src="{url}" width=100 height=100 />'.format(
            url = self.image.url,

            )
    )


@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    message = models.TextField()
