from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')
    fields = ('name', 'message')
    search_fields = ('name', 'message')


class Client_newsletterAdmin(admin.ModelAdmin):
    list_display = 'mail'
    fields = 'mail'
    search_fields = 'mail'


admin.site.register(Client)
admin.site.register(Client_newsletter)