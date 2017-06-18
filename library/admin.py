from django.contrib import admin

# Register your models here.

from .models import Platform, Videogame


# set up automated slug creation
class VideogameAdmin(admin.ModelAdmin):
    model = Videogame
    list_display = ('title', 'cover',)
    prepopulated_fields = {'slug': ('title',)}


class PlatformAdmin(admin.ModelAdmin):
    model = Platform
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Videogame, VideogameAdmin)
