from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import CollectionItem
from .forms import CollectionItemForm


# Create your views here.


def index(request, initial=None):
    if initial:
        items = CollectionItem.objects.filter(title__istartswith=initial).order_by('title')
    else:
        items = CollectionItem.objects.order_by('id')

    return render(request, 'library/index.html', {'items': items, 'initial': initial})


def detail(request, id):
    item = CollectionItem.objects.get(id=id)
    return render(request, 'library/detail.html', {'item': item})


@login_required
def edit(request, id):
    item = CollectionItem.objects.get(id=id)

    # make sure the logged in user is the owner of the thing
    if item.user != request.user:
        raise Http404

    form_class = CollectionItemForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=item)
        if form.is_valid():
            # save the new data
            form.save()

            messages.success(request, 'Item Updated.')
            return redirect('library:detail', id=item.id)
    # otherwise just create the form
    else:
        form = form_class(instance=item)
        # and render the template
        return render(request, 'library/edit.html', {'item': item, 'form': form})


@login_required
def add(request):
    form_class = CollectionItemForm
    # if we're coming from a submitted form, do this if request.method == 'POST':
    # grab the data from the submitted form and apply to # the form
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            item = form.save(commit=False)
            # set the additional details
            item.user = request.user
            # save the object
            item.save()

            messages.success(request, 'Item Added.')
            # redirect to our newly created thing
            return redirect('library:detail', id=item.id)
    # otherwise just create the form
    else:
        form = form_class()
        return render(request, 'library/create.html', {'form': form})

