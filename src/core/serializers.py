from rest_framework import serializers
from django.contrib.auth.models import User
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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
