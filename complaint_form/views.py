# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives

from .forms import *
from .models import *

from django.contrib.sites.shortcuts import get_current_site

from django.core import serializers

from easy_pdf.rendering import render_to_pdf

# Create your views here.


def fill_form(request):
    if request.method == 'GET':
        form = NewComplaintForm()
    else:
        form = NewComplaintForm(request.POST)
        if form.is_valid():

            submitted = form.save()



            current_site = get_current_site(request)

            mail_subject = 'Form Submission from ' + submitted.first_name + " " + submitted.last_name
            message = render_to_string('email.html', {
                'form': form,
                'domain': current_site.domain,
                'submitted': submitted,
            })

            post_pdf = render_to_pdf('email.html', {
                'form': form,
                'domain': current_site.domain,
                'submitted': submitted,
            })


            to_email = 'icrcformtest@gmail.com'
            email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'
            email.attach('' + submitted.first_name + '_' + submitted.last_name + '_complain_form.pdf', post_pdf, 'application/pdf')
            email.send()
            return redirect("/submitted")

    return render(request, 'form.html', {'form': form})


def submitted(request):
    return render(request, 'submitted.html')
