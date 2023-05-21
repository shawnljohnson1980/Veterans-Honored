from django.urls import include, path
from  .views import get_users, get_members

urlpatterns = [
    path('users/',get_users),
    path('members/',get_members),

]