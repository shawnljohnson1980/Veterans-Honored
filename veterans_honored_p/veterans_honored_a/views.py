from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(User):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(Group):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse('Hello World')