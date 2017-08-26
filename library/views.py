from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .models import MediaItem
from .forms import MediaItemForm, EditUserForm, UserSearchForm


# Create your views here.


def index(request, initial=None):
    if initial:
        items = MediaItem.objects.filter(title__istartswith=initial).order_by('title')
    else:
        items = MediaItem.objects.order_by('title')

    users = User.objects.order_by('username')
    form_class = UserSearchForm
    return render(request, 'library/index.html', {
        'items': items,
        'initial': initial,
        'users': users,
        'form': form_class
    })


def detail(request, slug):
    item = MediaItem.objects.get(slug=slug)
    return render(request, 'library/detail.html', {'item': item})


@login_required
def edit(request, slug):
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
            return redirect('library:detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=item)
        # and render the template
        return render(request, 'library/edit.html', {'item': item, 'form': form})


@login_required
def add(request):
    form_class = MediaItemForm
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
            return redirect('library:detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class()
        return render(request, 'library/add.html', {'form': form})


@login_required
def edit_profile(request):
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
        return render(request, 'library/edit_profile.html', {'user': user, 'form': form})

