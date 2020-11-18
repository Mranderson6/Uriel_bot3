from django.db import models

# Create your models here.
class client(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    mail = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    objet = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name