from django.conf.urls import url
from django.contrib.auth.models import User

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^(?P<pk>\d+)/$', GetPaper.as_view(), name='viewPaper'),
    # url(r'^$', ListPapers.as_view(), name='listPapers'),
    # url('^section/$', ListSections.as_view(), name='listSections'),
    url(r'^complaints/$', views.GetComplaints, name='getComplaints'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
