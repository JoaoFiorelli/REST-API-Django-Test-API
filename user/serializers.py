from rest_framework import serializers
from user import models


class UserProfileSerializer(serializers.ModelSerializer):
    """User Profile Serializer"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Cria um usuário"""

        user = models.UserProfile.objects.create(
            name=validated_data['name'], 
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user
