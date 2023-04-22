from rest_framework import viewsets
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
    serializer_class = ColeTablaSerializer


class EstudiantesTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesTabla.objects.all()
    serializer_class = EstudiantesTablaSerializer


class ModulosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer


class QuizTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizTabla.objects.all()
    serializer_class = QuizTablaSerializer


class SalonTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonTabla.objects.all()
    serializer_class = SalonTablaSerializer


class MonitorTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MonitorTabla.objects.all()
    serializer_class = MonitorTablaSerializer


class SalonKpiModuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonKpiModulo.objects.all()
    serializer_class = SalonKpiModuloSerializer
