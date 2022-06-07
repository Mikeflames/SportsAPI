from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db  import models

from typing import List
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from . models import *
from .serializers import *

#List and Create Player
class LCplayer(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = player.objects.all()
    serializer_class = playerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Retrieve, Update, Delete Player
class RUDplayer(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = player.objects.all()
    serializer_class = playerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# List and Create teacher
class LCteacher(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RUDteacher(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# List and Create sport
class LCsport(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = sports.objects.all()
    serializer_class = sportsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve Update and Delete sport
class RUDsport(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = sports.objects.all()
    serializer_class = sportsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# List and Create player sports
class LCplayer_sport(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = player_sport.objects.all()
    serializer_class = player_sportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve Update and Delete player sports
class RUDplayer_sport(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = player_sport.objects.all()
    serializer_class = player_sportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# List and Create teacher sports
class LCteacher_sport(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = teacher_sport.objects.all()
    serializer_class = teacher_sportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve Update and Delete teacher sports
class RUDteacher_sport(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = teacher_sport.objects.all()
    serializer_class = teacher_sportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LandingPage(APIView):
    def get(self, request):
        s = {'message' : 'Welcome', 'documentation' : '<specify notes>'}
        return Response(s)



'''
class sport(APIView):                 # inherits from an APIView
 
    def get(self, request):
        obj = sports_name.objects.all()      # Getting all values
        serializer = sports_nameSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        data = request.data             # Data passed in body
        serializer = sports_nameSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # if error


class sportbyid(APIView):    # Handle entry-specific operations
 
    def get_object(self,id):
        try:
            return sports_name.objects.get(id=id)
        except sports_name.DoesNotExist as e:
            return Response({"error": "Not found."},status=404)
    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = sports_name(instance) 
        return Response(serializer.data)
    def put(self, request, id=None):
        data = request.data            # Data passed to overwrite
        instance = self.get_object(id)   
        serializer = sports_nameSerializer(instance, data=data)   
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    def delete(self, request, id=None):
        instance = self.get_object(id)
        serializer = sports_nameSerializer(instance)
        instance.delete()
        return Response(serializer.data)    


class LandingPage(APIView):
    def get(self, request):
        s = {'message' : 'Welcome', 'documentation' : '<specify notes>'}
        return Response(s)

class player(APIView):                 # inherits from an APIView
 
    def get(self, request):
        obj = player.objects.all()      # Getting all values
        serializer = playerSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        data = request.data             # Data passed in body
        serializer = playerSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # if error

class playerbyid(APIView):    # Handle entry-specific operations
 
    def get_object(self, id):
        try:
            return player.objects.get(id=id)
        except player.DoesNotExist as e:
            return Response({"error": "Not found."},status=404)
    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = player(instance) 
        return Response(serializer.data)
    def put(self, request, id=None):
        data = request.data            # Data passed to overwrite
        instance = self.get_object(id)   
        serializer = playerSerializer(instance, data=data)   
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    def delete(self, request, id=None):
        instance = self.get_object(id)
        serializer = playerSerializer(instance)
        instance.delete()
        return Response(serializer.data)    



'''