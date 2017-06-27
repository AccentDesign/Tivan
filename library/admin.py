from django.contrib import admin
from .models import MediaFormat, MediaItem, CoverArt, Collection, CollectionItem


# set up automated slug creation
class MediaFormatAdmin(admin.ModelAdmin):
    model = MediaFormat
    list_display = ('platform',)


class MediaItemAdmin(admin.ModelAdmin):
    model = MediaItem
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CoverArtAdmin(admin.ModelAdmin):
    list_display = ('mediaItem',)
    list_display_links = ('mediaItem',)


class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    list_display = ('user',)


class CollectionItemAdmin(admin.ModelAdmin):
    model = CollectionItem
    list_display = ('item', 'format', 'collection',)


admin.site.register(MediaFormat, MediaFormatAdmin)
admin.site.register(MediaItem, MediaItemAdmin)
admin.site.register(CoverArt, CoverArtAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionItem, CollectionItemAdmin)
