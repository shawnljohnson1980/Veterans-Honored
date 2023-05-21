
from .models import User, Member
from rest_framework import serializers

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']

class Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['__all__']