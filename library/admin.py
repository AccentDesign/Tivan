from django.contrib import admin
from .models import Platform, MediaItem


# set up automated slug creation
class PlatformAdmin(admin.ModelAdmin):
    model = Platform
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}


class MediaItemAdmin(admin.ModelAdmin):
    model = MediaItem
    list_display = ('api_id', 'title', 'platform', 'available', 'cover_art_url', 'user')
    readonly_fields = ('slug',)


admin.site.register(Platform, PlatformAdmin)
admin.site.register(MediaItem, MediaItemAdmin)
