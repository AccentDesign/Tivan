from django.shortcuts import render, get_object_or_404
from .models import Videogame

# Create your views here.


def index(request):
    videogames = Videogame.objects.order_by('title')[:10]
    return render(request, 'library/index.html', {'videogames': videogames})


def detail(request, videogame_id):
    videogame = get_object_or_404(Videogame, pk = videogame_id)
    return render(request, 'library/detail.html', {'videogame': videogame})