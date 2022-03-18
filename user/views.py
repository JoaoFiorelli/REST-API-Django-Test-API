from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user import serializers
from user import models
from user import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Usuário ViewSet"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """Cria o token de autenticação"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
