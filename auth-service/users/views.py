from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email y contraseña requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, password=password)
        return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)