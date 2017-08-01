from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from registration.forms import RegistrationForm
from .forms import ContactForm

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

            context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content})
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


def how_it_works(request):
    return render(request, 'how-it-works.html')
