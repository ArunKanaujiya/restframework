from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from WebApp.models import *
from WebApp.serializers import *
# Create your views here.
@api_view(['GET'])
def get_book(request):
    book_objs=Book.objects.all()
    serializer=BookSerializer(book_objs,many=True)
    return Response({'status':200,'payload':serializer.data})


@api_view(['GET'])
def home(request):
    stud_obj=Student.objects.all()
    serializer=StudentSerializer(stud_obj,many=True)

    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    data=request.data
    serializer=StudentSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
    
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':'you sent '})

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        stud_obj=Student.objects.get(id=id)
        stud_obj.delete()
        return Response({'status':200,'message':'your data has deleted'})
    except Exception as e:
        return Response({'status':403,'message':'invalid id'}) 


@api_view(['PATCH'])
def update_student(request,id):
    try:
        student_obj=Student.objects.get(id=id)

        serializer=StudentSerializer(student_obj,data=request.data,partial=True)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'your data is update'})
    
    except Exception as e:
        return Response({'status':403,'message':'invalid id'})
    

@api_view(['PUT'])
def min_update_student(request,id):
    try:
        student_obj=Student.objects.get(id=id)

        serializer=StudentSerializer(student_obj,data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'your data is update'})
    
    except Exception as e:
        return Response({'status':403,'message':'invalid id'})