from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ('email', 'password')

    # ESTA FUNCIÓN ES CRÍTICA:
    # Asegura que se use tu UserManager y set_password, hasheando la clave.
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_admin')