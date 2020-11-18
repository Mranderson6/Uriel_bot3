from django import forms
from .models import *
from django.db import models



class contactForm(forms.Form):
    nom = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    objet = forms.CharField(required=True)
    message = forms.CharField(required=True)

