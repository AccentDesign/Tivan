from django.db import models

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=30)


class Videogame(models.Model):
    title = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    available = models.BooleanField(default=1)
