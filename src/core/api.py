from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import (ColeTabla, 
                     EstudiantesTabla, 
                     Modulos, 
                     QuizTabla, 
                     SalonTabla, 
                     MonitorTabla, 
                     SalonKpiModulo)
from .serializers import (ColeTablaSerializer, 
                          EstudiantesTablaSerializer, 
                          ModulosSerializer, 
                          QuizTablaSerializer, 
                          SalonTablaSerializer, 
                          MonitorTablaSerializer, 
                          SalonKpiModuloSerializer)


class ColeTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ColeTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ColeTablaSerializer


class EstudiantesTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EstudiantesTablaSerializer


class ModulosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modulos.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ModulosSerializer


class QuizTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuizTablaSerializer


class SalonTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonTablaSerializer


class MonitorTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MonitorTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MonitorTablaSerializer


class SalonKpiModuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonKpiModulo.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonKpiModuloSerializer
