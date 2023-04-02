from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from Landing.serializers import LoginSerializer,RegestrationSerializer
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProfileApiView(APIView):

    def post(self, request):
        
        user_data = {
            "email" : request.data["email"],
            "password" : request.data["password"],
            "username" : request.data["username"]
        }

        profile_data = {
            "image" : request.data["image"],
            "age" : request.data["age"]
        }
        print(user_data, profile_data)
       
        login_serializer = RegestrationSerializer(data=user_data)
        if login_serializer.is_valid():
            login_serializer.save()
            profile_data["user_id"] =login_serializer.data["id"]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
        serializer = ProfileSerializer(data=profile_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class ProfileTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "userForm.html"
    login_url = "/landing/sign-in"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'This is my data'
        return context