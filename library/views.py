from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import MediaItemForm, EditUserForm
from .models import MediaItem
from igdb_api_python.igdb import igdb

igdb = igdb("44abe2c0cd85cbc3b8d54ebfcf5d5de1")

# Create your views here.


@login_required
def welcome(request):
    result = igdb.games('legend of zelda')
    return render(request, 'welcome.html',{'result': result})


@login_required
def connection(request):
    return render(request, 'connection.html')


@login_required
def library(request, initial=None):
    if initial:
        items = MediaItem.objects.filter(title__istartswith=initial).order_by('title')
    else:
        items = MediaItem.objects.order_by('title')

    users = User.objects.exclude(username=request.user.username).order_by('username')
    return render(request, 'library/index.html', {
        'items': items,
        'initial': initial,
        'users': users,
    })


@login_required
def media_item_detail(request, slug):
    item = MediaItem.objects.get(slug=slug)
    return render(request, 'library/media_item_detail.html', {'item': item})


@login_required
def media_item_edit(request, slug):
    item = MediaItem.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if item.user != request.user:
        raise Http404

    form_class = MediaItemForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=item)
        if form.is_valid():
            # save the new data
            form.save()

            messages.success(request, 'Item Updated.')
            return redirect('media_item_detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=item)
        # and render the template
        return render(request, 'library/media_item_edit.html', {'item': item, 'form': form})


@login_required
def media_item_delete(request, slug):
    item = MediaItem.objects.get(slug=slug)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'The game has been deleted from your collection.')
        return redirect('your_collection')
    return render(request, 'library/media_item_delete.html', {'item': item})


@login_required
def collection(request):
    items = MediaItem.objects.filter(user=request.user).order_by('title')
    users = User.objects.exclude(username=request.user.username).order_by('username')

    form_class = MediaItemForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to # the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            item = form.save(commit=False)
            # set the additional details
            item.user = request.user

            # save the object
            item.save()

            messages.success(request, 'The game has been added to your collection.')
            # redirect to our newly created thing
            return redirect('your_collection')
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'library/your_collection.html', {
        'items': items,
        'users': users,
        'form': form,
    })


@login_required
def profile_edit(request):
    user = request.user
    form_class = EditUserForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile updated.')
            return redirect('index')
    else:
        form = form_class(instance=user)
        return render(request, 'library/profile_edit.html', {'user': user, 'form': form})
