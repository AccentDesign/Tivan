from django.db import models

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Videogame(models.Model):
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to = 'cover/', default = 'http://via.placeholder.com/250x350')
    available = models.BooleanField(default=1)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.title
