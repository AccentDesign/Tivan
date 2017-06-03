from django.shortcuts import render
from django.http import HttpResponse
from .models import Videogame

# Create your views here.


def index(request):
    videogames = Videogame.objects.order_by('title')[:10]
    output = ", ".join(v.title for v in videogames)
    return HttpResponse(output)


def detail(request, videogame_id):
    return HttpResponse("This is the detail view of the Videogame: %s" % videogame_id)
