from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', tarif,name='tarif'),

]
urlpatterns += staticfiles_urlpatterns()