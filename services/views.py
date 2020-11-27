from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import *
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'services/index.html')


def tarif(request):
    return render(request, 'services/tarif.html')


def adhesion(request):
    return render(request, 'services/adhesion/index.html')


def adhesion_login(request):
    return render(request, 'services/adhesion/home/sign_up.html')


def oublie_pwd(request):
    return render(request, 'services/adhesion/home/forgot_password.html')


def contact(request):
    return render(request, 'services/contact.html')


def contact_sendMail(request):
    sauvegarde = False
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            le_client = Client()
            le_client.name = form.cleaned_data['name']
            le_client.mail = form.cleaned_data['mail']
            le_client.phone = form.cleaned_data['phone']
            le_client.objet = form.cleaned_data['objet']
            le_client.message = form.cleaned_data['message']
            le_client.save()

            sauvegarde = True
            send_mail(le_client.objet, le_client.message, le_client.mail, ['akamabil@gmail.com'], fail_silently=False)

    else:
        form = ClientForm()
    return render(request, 'contact.html', locals())


def about(request):
    return render(request, 'services/about.html')
