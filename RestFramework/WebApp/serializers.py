from WebApp.models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','age','father_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        models=Book
        fields="__all__"

        