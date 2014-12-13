from django.shortcuts import render

from django.http import Http404

# Create your views here.
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import views

from .models import Todo
from .serializers import TodoSerializer, UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter, filters.DjangoFilterBackend]

class UserListApiView(views.APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(data=users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.DATA
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Create db entry
            user = User.objects.create(**serializer.data)
            return Response(serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

class UserDetailView(views.APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            raise Http404