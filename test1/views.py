from django.shortcuts import render
from .serializers import TestSerializer
from rest_framework import viewsets
from . models import Project_create


# Create your views here.
class Test1view(viewsets.ModelViewSet):
    queryset = Project_create.objects.all()
    serializer_class = TestSerializer  