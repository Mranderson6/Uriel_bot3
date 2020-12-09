from django.db import models
from django.contrib import admin


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    mail = models.CharField(max_length=200, null=True)
    objet = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        if self.name == None:
            return "ERROR-NAME IS NULL"
        return self.name


class Client_newsletter(models.Model):
    mail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.mail
