from rest_framework import serializers
from .models import SideMenuContent

class SideMenuSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SideMenuContent
        fields = ['name','is_head','url','svg','parent','child']

    def get_child(self,obj):
        query =  SideMenuContent.objects.filter(parent = obj.id)
        serializer = SideMenuSerializer(query,many=True)
        return serializer.data