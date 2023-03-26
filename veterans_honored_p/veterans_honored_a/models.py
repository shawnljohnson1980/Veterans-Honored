from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors={}
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email_pattern'] = "Email Address is invalid Please provide name@domain.com"
        if post_data['email']==['email']:
            errors ['email_unique']
        date_regex = re.compile("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$")
        if not date_regex.match(post_data['date']):
            errors ['date_pattern'] = "You must provide a valid date, for your Date of Birth"
        elif len(post_data['password']) < 8:
            errors['password_length'] = 'Password must be between 8 and 60 characters in length'
        if post_data['password'] != post_data['confirm_password']:
            errors['password_match'] = "passwords must match.."

        if len(post_data['first_name']) < 2 or len(post_data['first_name']) > 45:
            errors['first_name_length'] = 'first name should be at least 5 characters long, and no longer than 45 characters in length.'

        if len(post_data['last_name']) < 2 or len(post_data['last_name']) > 45:
            errors['last_name_length'] = 'last name should be at least 5 characters long, and no longer than 45 characters in length.'
        if len(post_data['user_name'])< 3 or len(post_data['user_name']) >80:
            errors['user_name_length'] = 'Your user name must be at least 3 characters long, and no longer than 80 characters'
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class MemberManager(models.Manager):
    def member_validator(self,post_data):
        errors={}
        if len(post_data['first_name']) < 2 or len(post_data['first_name']) > 45:
            errors['first_name_length'] = 'first name should be at least 2 characters long, and no longer than 45 characters in length.'
        if len(post_data['last_name']) < 2 or len(post_data['last_name']) > 45:
            errors['last_name_length'] = 'last name should be at least 2 characters long, and no longer than 45 characters in length.'
        
class Member(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    dob= models.DateField(editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MemberManager()
