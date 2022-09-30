from rest_framework import generics
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import Todo

from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

