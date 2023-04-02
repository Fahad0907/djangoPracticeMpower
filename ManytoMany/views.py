from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from .models import *
# Create your views here.
class BookApiView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        query = Book.objects.all()
        serializer = BookSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
