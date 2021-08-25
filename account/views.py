from rest_framework.views import APIView
from mysite.settings import DATABASES
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserCreateSerializer
from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class RegisterView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    permission_classes = [
        AllowAny
    ]
    '''
    mbti 질문과 보기를 반환하는 api
    ___
    '''
    def post(self, request, formet=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)