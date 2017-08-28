from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.http import Http404
from registration.forms import RegistrationForm
from .forms import ContactForm, MediaItemForm, EditUserForm
from library.models import MediaItem


# Create your views here.


def home(request):
    reg_form_class = RegistrationForm
    auth_form_class = AuthenticationForm
    return render(request, 'home.html', {'reg_form': reg_form_class, 'auth_form': auth_form_class,})


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # email the profile with the contact info
            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            })
            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Contact from Tivan',
                ['ben@accentdesign.co.uk'],
                headers={'Reply-To': contact_email}
            )
            email.send()

            messages.success(request, 'Message Sent.')
            return redirect('home')

    return render(request, 'contact.html', {'form': form_class})


def welcome(request):
    return render(request, 'welcome.html')


def connection(request):
    return render(request, 'connection.html')


@login_required
def library(request, initial=None):
    if initial:
        items = MediaItem.objects.filter(title__istartswith=initial).order_by('title')
    else:
        items = MediaItem.objects.order_by('title')

    users = User.objects.order_by('username')
    return render(request, 'library/index.html', {
        'items': items,
        'initial': initial,
        'users': users,
    })


@login_required
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
            return redirect('detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=item)
        # and render the template
        return render(request, 'library/edit.html', {'item': item, 'form': form})


@login_required
def collection(request):
    items = MediaItem.objects.order_by('title')
    users = User.objects.order_by('username')

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

            messages.success(request, 'Item Added.')
            # redirect to our newly created thing
            return redirect('your_collection', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'library/your_collection.html', {
        'items': items,
        'users': users,
        'form': form,
    })


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
