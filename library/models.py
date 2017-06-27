from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MediaFormat(models.Model):
    VIDEOGAME_PLATFORMS = (
        ('playstation-4', 'Sony PlayStation 4'),
        ('xbox-one', 'Xbox One'),
        ('nintendo-switch', 'Nintendo Switch'),
        ('playstation-3', 'Sony PlayStation 3'),
        ('xbox-360', 'Xbox 360'),
        ('nintendo-wii-u', 'Nintendo Wii U'),
    )
    platform = models.CharField(max_length=255, choices=VIDEOGAME_PLATFORMS)

    def __str__(self):
        return self.platform


class MediaItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.title


def get_image_path(instance, filename):
    return '/'.join(['cover-art', instance.mediaItem.slug, filename])


class CoverArt(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    mediaItem = models.OneToOneField(MediaItem, blank=True, null=True)


class Collection(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return self.id


class CollectionItem(models.Model):
    item = models.OneToOneField(MediaItem, blank=True, null=True)
    format = models.OneToOneField(MediaFormat, blank=True, null=True)
    collection = models.OneToOneField(Collection, blank=True, null=True)

    def __str__(self):
        return self.item.title

