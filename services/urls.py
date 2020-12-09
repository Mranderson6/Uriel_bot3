"""Uriel_Bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', index, name='index'),
    url('tarif/', tarif, name='tarif'),
    url('contact/', contact, name='contact'),
    url('about/', about, name='about'),
    url('^inscription/', adhesion_login, name='adhesion_login'),
    url('^sendMail/', contact_sendMail, name='contact_sendMail'),
    url('^newsletter/', contact_newsletter, name='contact_newsletter'),
    url('^adhesion/', adhesion, name='adhesion'),
    url('^oublie/', oublie_pwd, name='oublie_pwd'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
