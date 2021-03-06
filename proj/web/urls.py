from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^projects$', views.projects, name='projects')
]