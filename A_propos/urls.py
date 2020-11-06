from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', about,name='about'),

]
urlpatterns += staticfiles_urlpatterns()