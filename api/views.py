from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework import generics
from .models import Person


# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
