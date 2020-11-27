from django import forms
from .models import *
from django.db import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
