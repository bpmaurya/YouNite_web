from rest_framework import routers
from .viewsets import UserViewsets, ProfileViewsets

app_name = "core"
routers = routers.DefaultRouter()
routers.register('users',UserViewsets)
routers.register('profiles', ProfileViewsets)