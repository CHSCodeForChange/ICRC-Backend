from django.shortcuts import render, redirect
from complaint_form.models import *
from complaint_form.forms import *

from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from complaint_form.models import *

from rest_framework.response import Response

@api_view(['GET', 'POST'])
def GetComplaints(request):
    if request.method == 'GET':
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
