from django.contrib import admin
from .models import Work, ExpertTeam, Client
# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image','thumbnail',]
    
    # readonly_fields = ['image_tag']


@admin.register(ExpertTeam)
class ExpertTeamAdmin(admin.ModelAdmin):
    list_display = ['name','designation','image','thumbnail']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','designation','image','thumbnail']


