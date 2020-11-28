from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')
    fields = ('name', 'message')
    search_fields = ('name', 'message')





admin.site.register(Client)