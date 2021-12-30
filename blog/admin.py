from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','thumbnail','short_content']
    list_filter = ('category',)


    def short_content(self, obj):
        return mark_safe(obj.short_content)
    short_content.short_description = 'short_content'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']
