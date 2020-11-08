from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', adhesion,name='adhesion'),


]
urlpatterns += staticfiles_urlpatterns()