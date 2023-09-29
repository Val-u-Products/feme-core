from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from core.models import Usuarios

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if self.user:
            try:
                usuario = Usuarios.objects.get(email=self.user.email)
                id_v = usuario.id_v
                response.data['id_v'] = id_v
            except Usuarios.DoesNotExist:
                id_v = ""  # Si no se encuentra el usuario, asigna un valor vacío a id_v
                response.data['id_v'] = id_v

        return response
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer  # Asegúrate de importar tu serializador CustomUser
from .models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def create_superuser(request):
    if not request.user.is_superuser:
        return Response({"error": "No tienes permiso para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)

    # Crear una copia mutable de los datos
    data = dict(request.data)
    data['is_superuser'] = True  

    # Extraer la contraseña del JSON y configurarla correctamente
    password = data.pop('password', None)  # Extraer la contraseña del diccionario
    if password:
        user = CustomUser(**data)
        user.set_password(password)  # Configurar la contraseña utilizando set_password
        user.save()
        return Response({"message": "Usuario superadmin creado con éxito"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "La contraseña no se proporcionó"}, status=status.HTTP_400_BAD_REQUEST)



# from django.contrib.auth import authenticate, login, logout
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import UserSerializer


# class LoginView(APIView):
#     def post(self, request):

#         email = request.data.get('email', None)
#         password = request.data.get('password', None)
#         user = authenticate(email=email, password=password)

#         if user:
#             login(request, user)
#             return Response(
#                 UserSerializer(user).data,
#                 status=status.HTTP_200_OK)

#         return Response(
#             status=status.HTTP_404_NOT_FOUND)


# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)

#         return Response(status=status.HTTP_200_OK)
    

# class SignupView(generics.CreateAPIView):
#     serializer_class = UserSerializer