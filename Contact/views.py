from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    return render(request, 'contact.html')


def contact_sendMail(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail(contactForm, message, settings.EMAIL_HOST_USER, ['bigshow.stephane@gmail.com'], fail_silently=False)
    return render(request, 'contact.html')