from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.name


class Videogame(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='uploads/', default='uploads/placeholder-250x350.png')
    slug = models.SlugField(unique=True, default='')
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        return self.title
