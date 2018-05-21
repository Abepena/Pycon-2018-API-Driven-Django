from django.shortcuts import render
from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer
# Create your views here.

class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

