
from .models import User, Member
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','first_name','last_name', 'password','dob',]


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'username','first_name','last_name', 'password','dob','email','groups']
        
