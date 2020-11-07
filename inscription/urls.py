from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', adhesion,name='adhesion'),
    url(r'^enregistrement$', adhesion_login,name='adhesion_login'),

]
urlpatterns += staticfiles_urlpatterns()