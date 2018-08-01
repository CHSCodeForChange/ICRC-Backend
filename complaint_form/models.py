# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.localflavor.us.models import USStateField

from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.


class Complaint(models.Model):
    objects = models.Manager()

    first_name = models.CharField(max_length=128) # fillers first name
    last_name = models.CharField(max_length=128) # fillers last name

    email = models.EmailField() # fillers email address
    phone_number = PhoneNumberField() # fillers phonenumber
    address = models.CharField(max_length=128) # filler's home address
    city = models.CharField(max_length=64) # filler's home city
    state = models.CharField(max_length=3, default="IN") # filler's home state (default is 'IN' as this form is mainly for Indiana residents)
    zip_code = models.IntegerField() # the filler's home zip code 

    discrimination_description = models.CharField(max_length=2000) # the filler's description of the discrimination that he or she faced

    offending_party = models.CharField(max_length=128) # the offending party: person or business
    OFFENDER_TYPE_CHOICES = ((1, 'Business'), (2, 'Person'))
    offender_type = models.CharField(max_length=32, choices=OFFENDER_TYPE_CHOICES) # the type of party that offended the form filler 
    offender_phone_number = PhoneNumberField() # the phone number of the offender
    offender_address = models.CharField(max_length=128, null=True) # the street address of the offender, optional
    offender_city = models.CharField(max_length=64, null=True) # the city of the offender, optional
    offender_state = models.CharField(max_length=2, default="IN", null=True) # the state of the offender, optional
    offender_zip_code = models.IntegerField(null=True) # the zip code of the offender, optional

    DESCRIMINATION_TYPE_CHOICES = (
        (1, 'Employment (terminated, hours cut, suspended, denied employment, etc.)'),
        (2, 'Housing (evicted, denied a house or apartment, subjected to different terms and conditions, etc.)'),
        (3, 'Public Accommodation (denied access to services, etc.)'),
        (4, 'Credit (denied a loan, subjected to different terms or conditions, etc.)'), 
        (5, 'Education (special education services, disparate discipline, etc.)')
    )
    descrimination_type = models.CharField(max_length=128, choices=DESCRIMINATION_TYPE_CHOICES) # the way in which the filler was treated unfairly
    descrimination_date = models.DateField() # the date the descrimination occured


    DESCRIMINATION_BASIS_CHOICES = (
        (1, 'Age'),
        (2, 'Ancestry'),
        (3, 'Color'),
        (4, 'Disability'), 
        (5, 'Race'), 
        (6, 'Religion'),
        (7, 'Sex'),
        (8, 'Retaliation'),
        (9, 'Familial Status'),
        (10, 'National Origin')
    )
    descrimination_basis = models.CharField(max_length=32, choices=DESCRIMINATION_BASIS_CHOICES) # the reason the filler feels they were descriminated for

    REFERENCE_CHOICES = (
        (1, 'Attorney/Lawyer'),
        (2, 'Government Agency'),
        (3, 'Friend'),
        (4, 'Advertisement'), 
        (5, 'Brochure/Poster'), 
        (6, 'Internet'),
    )
    reference = models.CharField(max_length=32, choices=REFERENCE_CHOICES) # the party that informed the filler of the form

    signature = models.CharField(max_length=256) # this consists of the filler's first and last name

   