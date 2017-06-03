from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Videogame

# Create your views here.


def index(request):
    videogames = Videogame.objects.order_by('title')[:10]
    template = loader.get_template('library/index.html')
    context = RequestContext(request, {
        'videogames':videogames
    })
    return HttpResponse(template.render(context))


def detail(request, videogame_id):
    return HttpResponse("This is the detail view of the Videogame: %s" % videogame_id)
