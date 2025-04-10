from django.contrib import admin
from .models import *


# Register your models here.
class Videoadmin(admin.ModelAdmin):
    def show_title(self):
        return self.title

    list_display = ("id" ,"title" , show_title  ,"published_date" , "short_details")
admin.site.register(Video ,Videoadmin)
