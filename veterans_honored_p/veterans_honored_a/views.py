from django.shortcuts import render
from .models import User, Member
from .serializers import UserSerializer, MemberSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

def index(request):
    return HttpResponse('Hello World')

def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data =JSONParser.parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 202)
        return JsonResponse(serializer.errors, status = 400)
    
def get_members(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 202)
        return JsonResponse(serializer.errors, status = 400)