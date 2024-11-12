from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
# Create your views here.

class Student_API(APIView):
    def get(self, request):
        return Response(data={'msg': 'Hello World'})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print('DESERIALIZE-->', serializer.data)
        return Response(data={'msg': 'Record Added'})