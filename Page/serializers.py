from rest_framework import serializers
from .models import PageComponent,Page

class PageSerializer(serializers.ModelSerializer):
    page_component = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Page
        fields = ['id','banner_image','title']

class PageComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageComponent
        fields = '__all__'