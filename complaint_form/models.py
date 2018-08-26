# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.localflavor.us.models import USStateField

from phonenumber_field.modelfields import PhoneNumberField


class Complaint(models.Model):
    objects = models.Manager()

    first_name = models.CharField(max_length=128, null=True, blank=True) # fillers first name
    last_name = models.CharField(max_length=128) # fillers last name

    email = models.EmailField() # fillers email address
    phone_number = PhoneNumberField() # fillers phonenumber
    address = models.CharField(max_length=128) # filler's home address
    city = models.CharField(max_length=64) # filler's home city
    state = models.CharField(max_length=3, default="IN") # filler's home state (default is 'IN' as this form is mainly for Indiana residents)
    zip_code = models.IntegerField() # the filler's home zip code

    secondary_first_name = models.CharField(max_length=128, default=None, null=True, blank=True) # fillers first name
    secondary_last_name = models.CharField(max_length=128, default=None, null=True, blank=True) # fillers last name

    secondary_email = models.EmailField(default=None, null=True, blank=True) # fillers email address
    secondary_phone_number = PhoneNumberField(default=None, null=True, blank=True) # fillers phonenumber
    secondary_address = models.CharField(max_length=128, default=None, null=True, blank=True) # filler's home address
    secondary_city = models.CharField(max_length=64, default=None, null=True, blank=True) # filler's home city
    secondary_state = models.CharField(max_length=3, default="IN", null=True, blank=True) # filler's home state (default is 'IN' as this form is mainly for Indiana residents)
    secondary_zip_code = models.IntegerField(default=None, null=True, blank=True) # the filler's home zip code



    offending_party = models.CharField(max_length=128) # the offending party: person or business
    OFFENDER_TYPE_CHOICES = (('1', 'Business'), ('2', 'Person'))
    offender_type = models.CharField(max_length=32, choices=OFFENDER_TYPE_CHOICES) # the type of party that offended the form filler
    offender_phone_number = PhoneNumberField() # the phone number of the offender
    offender_address = models.CharField(max_length=128, null=True) # the street address of the offender, optional
    offender_city = models.CharField(max_length=64, null=True) # the city of the offender, optional
    offender_state = models.CharField(max_length=2, default="IN", null=True) # the state of the offender, optional
    offender_zip_code = models.IntegerField(null=True) # the zip code of the offender, optional
    offender_number_of_employees = models.IntegerField(null=True)

    DISCRIMINATION_TYPE_CHOICES = (
        ('1', 'Employment (terminated, hours cut, suspended, denied employment, etc.)'),
        ('2', 'Housing (evicted, denied a house or apartment, subjected to different terms and conditions, etc.)'),
        ('3', 'Public Accommodation (denied access to services, etc.)'),
        ('4', 'Credit (denied a loan, subjected to different terms or conditions, etc.)'),
        ('5', 'Education (special education services, disparate discipline, etc.)')
    )
    discrimination_type = models.CharField(max_length=128, choices=DISCRIMINATION_TYPE_CHOICES) # the way in which the filer was treated unfairly
    discrimination_date = models.DateField(default=None) # the date the discrimination occured


    DISCRIMINATION_BASIS_CHOICES = (
        ('1', 'Age'),
        ('2', 'Ancestry'),
        ('3', 'Color'),
        ('4', 'Disability'),
        ('5', 'Race'),
        ('6', 'Religion'),
        ('7', 'Sex'),
        ('8', 'Retaliation'),
        ('9', 'Familial Status'),
        ('10', 'National Origin')
    )
    discrimination_basis = models.CharField(max_length=32, choices=DISCRIMINATION_BASIS_CHOICES) # the reason the filler feels they were descriminated for

    REFERENCE_CHOICES = (
        ('1', 'Attorney/Lawyer'),
        ('2', 'Government Agency'),
        ('3', 'Friend'),
        ('4', 'Advertisement'),
        ('5', 'Brochure/Poster'),
        ('6', 'Internet'),
    )
    reference = models.CharField(max_length=32, choices=REFERENCE_CHOICES) # the party that informed the filler of the form

    related_offender_name = models.CharField(max_length=200, default=None, null=True, blank=True) #the party whose grievance or other action is related to this particular complaint
    date_filed = models.DateField(default=None, null=True, blank=True) #the date that the related complaint was filed
    status_or_disposition = models.CharField(max_length=200, default=None, null=True, blank=True) #the status or disposition of the related complaint
    date_of_disposition = models.DateField(default=None, null=True, blank=True) #the date of the disposition of the related complaint
    date_of_act = models.DateField(default=None, null=True, blank=True) #the date of the act of which the related complaint concerns

    discrimination_description = models.CharField(max_length=2000, default=None) # the filler's description of the discrimination that he or she faced
    signature = models.CharField(max_length=256) # this consists of the filler's first and last name
    date = models.DateField(default=None) #date of signature/form submission
