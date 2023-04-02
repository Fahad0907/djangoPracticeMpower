from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PageSerializer,PageComponentSerializer
from django.db import transaction
import json
# Create your views here.
class PageApi(APIView):
    def post(self, request):
        page_id = 0

        page = {
            "banner_image": request.data['banner_image'],
            "user_id" : request.data['user_id'],
            "title" : request.data["title"]
        }
        page_serializer = PageSerializer(data=page)
        if page_serializer.is_valid():
            page_id = page_serializer.save()
            page_id = page_id.id
        else:
            return Response(page_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        

        text_data = json.loads(request.data['textdata'])
        for text  in text_data:
            text_data_dic = dict()
            text_data_dic["page"] = page_id
            text_data_dic["richtext"] = text
            print(text_data_dic)
            serializer = PageComponentSerializer(data=text_data_dic)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
        return Response(status=status.HTTP_201_CREATED)
    

class PageDetials(APIView):
    def get(self ,request):
        pass
