from django.shortcuts import render
from django.template.defaultfilters import slugify
from library.forms import VideogameForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


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
        # redirect to our newly created thing
        return redirect('library/detail', slug=item.slug)
    # otherwise just create the form
    else:
        form = form_class()
        return render(request, 'library/create.html', { 'form': form, })