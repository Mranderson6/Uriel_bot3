from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', adhesion, name='adhesion'),
    url(r'^oublie/$', oublie_pwd, name='oublie_pwd'),

]
urlpatterns += staticfiles_urlpatterns()