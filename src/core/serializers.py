from rest_framework import serializers
from .models import ColeTabla, EstudiantesTabla, Modulos, QuizTabla, SalonTabla


class ColeTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColeTabla
        fields = '__all__'


class EstudiantesTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantesTabla
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
