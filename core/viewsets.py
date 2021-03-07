from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly


class UserViewsets(viewsets.ModelViewSet):
    permission_classes={IsUserOwnerOrGetAndPostOnly,}
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class ProfileViewsets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
