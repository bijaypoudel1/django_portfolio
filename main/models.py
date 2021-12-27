from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    image = models.ImageField()


    def thumbnail(self):
        return mark_safe('<img src="{url}" width=100 height=100 />'.format(
            url = self.image.url,
            )
    )


class ExpertTeam(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    image = models.ImageField(null = True)
    facebook= models.CharField(max_length=100, default="#")
    instagram = models.CharField(max_length=100, default="#")
    twitter = models.CharField(max_length=100, default="#")


    def thumbnail(self):
        return mark_safe('<img src="{url}" width=100 height=100 />'.format(
            url = self.image.url,

            )
    )

class Client(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    image = models.ImageField(null = True)
    description = models.TextField(max_length=500)

    def thumbnail(self):
        return mark_safe('<img src="{url}" width=100 height=100 />'.format(
            url = self.image.url,

            )
    )
















