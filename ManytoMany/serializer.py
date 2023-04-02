from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    author_list = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id','name', 'author_list']

    def create(self, validated_data):
        print(validated_data)
        author_data = validated_data.pop('author_list',[])
        print(author_data)
        book = Book.objects.create(**validated_data)

        for author in author_data:
            author_instance = Author.objects.get(pk=author['id'])
            book.author_list.add(author_instance)
        
        return book