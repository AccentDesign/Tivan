from django.contrib import admin

# Register your models here.

from .models import Platform, Videogame

admin.site.register(Platform)
admin.site.register(Videogame)
