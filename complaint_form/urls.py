
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url('^$', views.fill_form),
    url('^submitted/$', views.submitted)
]
