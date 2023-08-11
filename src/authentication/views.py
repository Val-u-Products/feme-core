from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from core.models import Usuarios

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if self.user:
            usuario = Usuarios.objects.get(email=self.user.email)
            id_v = usuario.id_v
            response.data['id_v'] = id_v

        return response

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