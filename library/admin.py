from django.contrib import admin

# Register your models here.

from .models import Platform, Videogame


# set up automated slug creation
class VideogameAdmin(admin.ModelAdmin):
    model = Videogame
    list_display = ('title', 'platform', 'cover', 'available',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Platform)
admin.site.register(Videogame, VideogameAdmin)
