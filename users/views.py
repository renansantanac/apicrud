from django.shortcuts import render

from rest_framework import generics
from .models import User
from .serializer import UserSerializer


# Criar um usuário e exibi-lo
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Para recuperar, atualizar ou excluir um usuário pelo ID
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer