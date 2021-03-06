from rest_framework import routers
from .viewsets import UserViewsets

app_name = "core"
routers = routers.DefaultRouter()
routers.register('users',UserViewsets)