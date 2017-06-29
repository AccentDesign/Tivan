from django.contrib import admin
from .models import Platform, MediaItem


# set up automated slug creation
class PlatformAdmin(admin.ModelAdmin):
    model = Platform
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MediaItemAdmin(admin.ModelAdmin):
    model = MediaItem
    list_display = ('title', 'platform', 'coverArt', 'available', 'user')
    prepopulated_fields = {'slug': ('title', 'platform', 'user')}


admin.site.register(Platform, PlatformAdmin)
admin.site.register(MediaItem, MediaItemAdmin)
