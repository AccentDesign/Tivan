from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.


def get_image_path(instance, filename):
    return '/'.join(['images', instance.slug, filename])


class Platform(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to=get_image_path, default='')
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.name


class MediaItem(models.Model):
    api_id = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, default='')
    cover_art_url = models.CharField(max_length=255, default='')
    available = models.BooleanField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.title


class Connection(models.Model):
    users = models.ManyToManyField(User, blank=True)
    active = models.BooleanField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    connections = models.ManyToManyField(Connection, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

