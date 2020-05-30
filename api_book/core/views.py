from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer


class Book_ViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

