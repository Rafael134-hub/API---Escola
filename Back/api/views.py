from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
import json


# Create your views here.
class TeacherAPIView(views.APIView):

    def post(self, request):

        queryset= request.data
        teacherSerialized = TeacherSerializer(data = queryset)
        teacherSerialized.is_valid(raise_exception = True)
        teacherSerialized.save()
        return Response(status = status.HTTP_201_CREATED)
    
    def put(self, request, teacher):
        try:
            updated_teacher = Teacher.objects.get(name = teacher)
        except: 
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherSerializer(updated_teacher, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, teacher = None):
        try:
           teacher_to_delete = Teacher.objects.get(name = teacher)
           teacher_to_delete.delete()
           return Response(status = status.HTTP_202_ACCEPTED)
        
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, teacher=None, pk = None):

        if teacher:
            try:
                queryset = Teacher.objects.get(name = teacher)
                serializer = TeacherSerializer(queryset)
                return Response(serializer.data)
            
            except Teacher.DoesNotExist:
                return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            queryset = Teacher.objects.all()
            serializer = TeacherSerializer(queryset, many = True)
            return Response(serializer.data)

        

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_professores(request, id=None):

    if request.method == 'GET':
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class TheachersView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions_classes = [IsAuthenticated]

class TeachersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer