from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from JFFIU_app.forms import *
from templates import *
from django.contrib import messages
from django.template.loader import get_template


@login_required
def contactView(request):
    if request.method == 'GET':
        Contact_Form = ContactForm()
        return render(request, 'contact.html', {'form': Contact_Form})
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():

            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('templates/contact_form.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['grteam.tht131417@gmail.com'],
                # header = { 'Reply To': contact_email }
            )
        email.send()
        return redirect('success-send')


@login_required
def successView(request):
    messages.info(request, "Success! Thank you for your message.")
    return redirect('home')
