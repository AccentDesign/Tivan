from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Videogame
from .forms import VideogameForm


# Create your views here.


def index(request, initial=None):
    if initial:
        videogames = Videogame.objects.filter(title__istartswith=initial).order_by('title')
    else:
        videogames = Videogame.objects.order_by('title')

    return render(request, 'library/index.html', {'videogames': videogames, 'initial': initial})


def detail(request, slug):
    videogame = Videogame.objects.get(slug=slug)
    return render(request, 'library/detail.html', {'videogame': videogame})


@login_required
def edit(request, slug):
    videogame = Videogame.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if videogame.user != request.user:
        raise Http404

    form_class = VideogameForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=videogame)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('library:detail', slug=videogame.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=videogame)
        # and render the template
        return render(request, 'library/edit.html', {'videogame': videogame, 'form': form})
