from rest_framework import serializers
from complaint_form.models import *

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        exclude = []
