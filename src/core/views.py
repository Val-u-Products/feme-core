# import secrets
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import MonitorTabla
#from .serializers import UserSerializer


# class UserRegistration(APIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Inicio de sesión exitoso'})
#         else:
#             return Response({'message': 'Correo electrónico o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     return Response({'message': 'Sesión cerrada'})


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def actualizar_key(request, pk):
#     print(pk)
#     try:
#         monitor = MonitorTabla.objects.get(pk=pk)
#     except MonitorTabla.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     nueva_key = secrets.token_urlsafe(12)
#     monitor.userToken = nueva_key
#     monitor.save()
    
#     return Response({'userToken': nueva_key}, status=status.HTTP_200_OK)

# class ActualizarKeyView(APIView):
#     def patch(self, request, uuid_mont):
#         try:
#             monitor = MonitorTabla.objects.get(uuid_mont=uuid_mont)
#         except MonitorTabla.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         nueva_key = secrets.token_urlsafe(16)
#         monitor.key = nueva_key
#         monitor.save()
        
#         return Response({'key': nueva_key}, status=status.HTTP_200_OK)