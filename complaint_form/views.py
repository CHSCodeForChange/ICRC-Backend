# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.


def fill_form(request):
    if request.method == 'GET':
        form = NewComplaintForm()
    else:
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            group = form.save()

            return redirect("/submitted")

    return render(request, 'form.html', {'form': form})


def submitted(request):
    return render(request, 'submitted.html')


