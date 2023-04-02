from django.shortcuts import render
from .models import Content, ContentHeading
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SideMenuContent
from .serializers import SideMenuSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.

class SideMenuList(APIView):

    def get(self,request):
        query = SideMenuContent.objects.filter(is_head=True)
        serializers = SideMenuSerializer(query,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

def my_context_processor(request):
    query = Content.objects.all()
    side_menu_list = SideMenuList()
    response = side_menu_list.get(request)
    return {'content_data_testing': response.data}
def show(request):
    # query = Content.objects.all()
    # print(query)
    return render(request,'firstsection.html')

def base(request):
    # query = Content.objects.all()
    # print(query)
    return render(request,'base.html')


@login_required(login_url='/landing/sign-in')
def secondSetion(request):
    return render(request,'secondSection.html')

def thirdSection(request):
    return render(request,'thirdsection.html')

# def home(request):
#     return render(request, 'home.html')

def fourthsection(request):
    return render(request, 'fourthSection.html')