from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from .forms import ContactForm
from library.forms import VideogameForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


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

            context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content})
            content = template.render(context)
            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <hi@weddinglovely.com>',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email}
            )
            email.send()

            messages.success(request, 'Message Sent.')
            return redirect('home')

    return render(request, 'contact.html', {'form': form_class})


def add_item(request):
    form_class = VideogameForm
    # if we're coming from a submitted form, do this if request.method == 'POST':
    # grab the data from the submitted form and apply to # the form
    form = form_class(request.POST)
    if form.is_valid():
        # create an instance but do not save yet
        item = form.save(commit=False)
        # set the additional details
        item.user = request.user
        item.slug = slugify(item.name)
        # save the object
        item.save()

        messages.success(request, 'Item Added.')
        # redirect to our newly created thing
        return redirect('library/detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class()
        return render(request, 'library/create.html', { 'form': form, })