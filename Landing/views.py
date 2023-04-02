from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import User
from .serializers import LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginTemplateView(TemplateView):
    template_name = "sign-in.html"

# Create your views here.
def base_landing_page(request):
    print(request.user)
    return render(request,'landing.html')

def sign_in(request):
    
    return render(request, 'sign-in.html')

def loginCheck(request):
    if request.method == "POST" or request.method == "post":
        print("post working")

class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user :
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    # def get(self,request):
    #     return Response(status=status.HTTP_200_OK)

class RichTextTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "richtext.html"

class PracticeTemplateView(TemplateView):
    template_name = "practice.html"