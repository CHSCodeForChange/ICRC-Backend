# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-11 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(default='IN', max_length=3)),
                ('zip_code', models.IntegerField()),
                ('secondary_first_name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('secondary_last_name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('secondary_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('secondary_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True)),
                ('secondary_address', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('secondary_city', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('secondary_state', models.CharField(blank=True, default='IN', max_length=3, null=True)),
                ('secondary_zip_code', models.IntegerField(blank=True, default=None, null=True)),
                ('offending_party', models.CharField(max_length=128)),
                ('offender_type', models.CharField(choices=[('1', 'Business'), ('2', 'Person')], max_length=32)),
                ('offender_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('offender_address', models.CharField(max_length=128, null=True)),
                ('offender_city', models.CharField(max_length=64, null=True)),
                ('offender_state', models.CharField(default='IN', max_length=2, null=True)),
                ('offender_zip_code', models.IntegerField(null=True)),
                ('offender_number_of_employees', models.IntegerField(null=True)),
                ('discrimination_type', models.CharField(choices=[('1', 'Employment (terminated, hours cut, suspended, denied employment, etc.)'), ('2', 'Housing (evicted, denied a house or apartment, subjected to different terms and conditions, etc.)'), ('3', 'Public Accommodation (denied access to services, etc.)'), ('4', 'Credit (denied a loan, subjected to different terms or conditions, etc.)'), ('5', 'Education (special education services, disparate discipline, etc.)')], max_length=128)),
                ('discrimination_date', models.DateField(default=None)),
                ('discrimination_basis', models.CharField(choices=[('1', 'Age'), ('2', 'Ancestry'), ('3', 'Color'), ('4', 'Disability'), ('5', 'Race'), ('6', 'Religion'), ('7', 'Sex'), ('8', 'Retaliation'), ('9', 'Familial Status'), ('10', 'National Origin')], max_length=32)),
                ('reference', models.CharField(choices=[('1', 'Attorney/Lawyer'), ('2', 'Government Agency'), ('3', 'Friend'), ('4', 'Advertisement'), ('5', 'Brochure/Poster'), ('6', 'Internet')], max_length=32)),
                ('related_offender_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_filed', models.DateField(blank=True, default=None, null=True)),
                ('status_or_disposition', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_of_disposition', models.DateField(blank=True, default=None, null=True)),
                ('date_of_act', models.DateField(blank=True, default=None, null=True)),
                ('discrimination_description', models.CharField(default=None, max_length=2000)),
                ('signature', models.CharField(max_length=256)),
                ('date', models.DateField(default=None)),
            ],
        ),
    ]
