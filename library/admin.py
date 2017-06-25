from django.contrib import admin

# Register your models here.

from .models import MediaFormat, MediaItem, Collection, CollectionItem


# set up automated slug creation
class MediaFormatAdmin(admin.ModelAdmin):
    model = MediaFormat
    list_display = ('platform',)


class MediaItemAdmin(admin.ModelAdmin):
    model = MediaItem
    list_display = ('title', 'cover',)
    prepopulated_fields = {'slug': ('title',)}


class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    list_display = ('user',)


class CollectionItemAdmin(admin.ModelAdmin):
    model = CollectionItem
    list_display = ('item', 'format', 'collection',)


admin.site.register(MediaFormat, MediaFormatAdmin)
admin.site.register(MediaItem, MediaItemAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionItem, CollectionItemAdmin)
