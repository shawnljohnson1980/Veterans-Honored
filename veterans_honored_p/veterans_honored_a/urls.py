from django.urls import include, path
from rest_framework import routers
from .import views



router = routers.SimpleRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.index),
    path('',views.get_users),
    path('',views.get_members),

]