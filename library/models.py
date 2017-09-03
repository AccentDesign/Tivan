from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


def get_image_path(instance, filename):
    return '/'.join(['images', instance.slug, filename])


class Platform(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to=get_image_path, default='')
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class MediaItem(models.Model):
    api_id = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, default='')
    cover_art_url = models.CharField(max_length=255, default='')
    available = models.BooleanField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    slug = models.SlugField(null=True, blank=True, unique=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('%s %s %s' % (self.title, self.platform.slug, self.user.username))
        super(MediaItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Connection(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(User, blank=True)
    active = models.BooleanField(default=0)

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

