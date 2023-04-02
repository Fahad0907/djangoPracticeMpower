from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
        extra_kwargs = {'password' : {'write_only' : True}}
    



class RegestrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','username']

    def create(self, validateData):
        return User.objects.create_user(**validateData)