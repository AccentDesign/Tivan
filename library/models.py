from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.name


def get_image_path(filename):
    return '/'.join(['cover-art', filename])


class MediaItem(models.Model):
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, default='')
    coverArt = models.ImageField(upload_to=get_image_path, default='')
    available = models.BooleanField(default=1)
    slug = models.SlugField(unique=True, default='')
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return self.title


class Connection(models.Model):
    users = models.ManyToManyField(User, blank=True)
    active = models.BooleanField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    connections = models.ManyToManyField(Connection, blank=True)

