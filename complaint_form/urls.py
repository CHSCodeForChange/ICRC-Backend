
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.fill_form),
    url(r'^submitted', views.submitted),
]
