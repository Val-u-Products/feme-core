from rest_framework import serializers
from .models import (ColeTabla, 
                     EstudiantesTabla,
                     Modulos, QuizTabla, 
                     SalonTabla, 
                     MonitorTabla, 
                     SalonKpiModulo,
                     Estatus,
                     Monitoreo,
                     Feedback
                     )


class ColeTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColeTabla
        fields = '__all__'


class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'


class QuizTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTabla
        fields = '__all__'


class SalonTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonTabla
        fields = '__all__'


class MonitorTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorTabla
        fields = '__all__'


class EstudiantesTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesTabla
        fields = '__all__'


class SalonKpiModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonKpiModulo
        fields = '__all__'


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = '__all__'


class MonitoreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoreo
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
