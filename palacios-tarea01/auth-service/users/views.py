from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Importamos los Serializers que definiste en users/serializers.py
from .serializers import UserSerializer, MeSerializer 

class RegisterView(generics.CreateAPIView):
    """
    Vista para el registro de nuevos usuarios.
    Utiliza UserSerializer para validar y crear el usuario.
    Permite el acceso a cualquier usuario (AllowAny).
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class MeView(APIView):
    """
    Vista para ver el perfil del usuario autenticado.
    Requiere que el usuario esté logueado (IsAuthenticated).
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # El objeto 'request.user' contiene la instancia del usuario autenticado
        serializer = MeSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)