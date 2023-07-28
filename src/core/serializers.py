# import random
# import string
# import uuid
# import re
# from django.db.models import Sum
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (ColegioTabla,
                     SalonTabla, 
                     Rol,
                     Usuarios,
                     ValuThinkific,
                     EstatusThinkific,
                     EstatusValu,
                     Modulos,
                     ContenidosColegio,
                     ModuloContenido,
                     QuizTabla,
                     Feedback,
                     Monitoreo,
                     Jerarquium,
                     SalonInfoProfe,
                     EstProfe,
                     EstatusGeneral,
                     # SalonKpiModulo
                     )


class ColegioTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColegioTabla
        fields = '__all__'


class SalonTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonTabla
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class ValuThinkificSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValuThinkific
        fields = '__all__'


# class EstudiantesTablaSerializer(serializers.ModelSerializer):
#     modulos = serializers.SerializerMethodField() # New line
#     nota_promedio = serializers.SerializerMethodField()
#     ranking = serializers.SerializerMethodField()

#     class Meta:
#         model = EstudiantesTabla
#         # fields test
#         fields = [
#             'id_thinkific',
#             'uuid_salon',
#             'colegio',
#             'grado',
#             'seccion',
#             'nombres_estudiantes',
#             'apellidos_estudiantes',
#             'email',
#             'whatsapp_estudiante',
#             'nombres_representante',
#             'apellidos_representante',
#             'whatsapp_representante',
#             'email_representante',
#             'inscrito',
#             'uuid_mont',
#             'uuid_cole',
#             'nota_promedio',
#             'ranking',
#             'modulos'
#         ]

#     # New func
#     def get_modulos(self, obj):
#         estatus = Estatus.objects.filter(id_thinkific=obj.id_thinkific)
#         serializer = ModuloSerializer(instance=estatus, many=True)
#         return serializer.data
    
#     def get_estudiantes_con_promedio_y_modulos(self, obj):
#         estudiantes_con_promedio_y_modulos = EstudiantesConPromedioYModulos.objects.get(id_thinkific=obj.id_thinkific)
#         return estudiantes_con_promedio_y_modulos
    
#     def get_nota_promedio(self, obj):
#         estudiantes_con_promedio_y_modulos = self.get_estudiantes_con_promedio_y_modulos(obj)
#         return estudiantes_con_promedio_y_modulos.nota_promedio
    
#     def get_ranking(self, obj):
#         estudiantes_con_promedio_y_modulos = self.get_estudiantes_con_promedio_y_modulos(obj)
#         return estudiantes_con_promedio_y_modulos.ranking


# class EstudiantesConPromedioYModulosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EstudiantesConPromedioYModulos
#         # fields = '__all__'
#         fields = [
#             'id_thinkific',
#             'nota_promedio',
#             'ranking'
#         ]
        


# class SalonKpiModuloSerializer(serializers.ModelSerializer):
#     top_estudiantes = serializers.SerializerMethodField()
#     promedio_salon = serializers.SerializerMethodField()

#     class Meta:
#         model = SalonKpiModulo
#         fields = [
#             'id_skm',
#             'uuid_salon',
#             'id_mol',
#             'grado',
#             'seccion',
#             'modulo',
#             'total_estudiantes',
#             'iniciaron',
#             'llevan50',
#             'completaron',
#             'created_at',
#             'top_estudiantes',
#             'promedio_salon'
#         ]

#     def get_top_estudiantes(self, obj):
#         uuid_salon = str(obj.uuid_salon)
        
#         match = re.search(r'\((.*?)\)', uuid_salon)
#         uuid_salon = match.group(1)
#         estudiantes = EstudiantesConPromedioYModulos.objects.filter(uuid_salon=uuid_salon)

#         request = self.context.get('request')
#         orden = request.GET.get('orden', 'descendente')

#         campo_orden = ['-ranking'] if orden == 'descendente' else ['ranking']

#         estudiantes = estudiantes.order_by(*campo_orden)[:5]

#         serializer = EstudiantesConPromedioYModulosSerializer(instance=estudiantes, many=True)
#         return serializer.data

#     def get_promedio_salon(self, obj):
#         uuid_salon = str(obj.uuid_salon)
        
#         match = re.search(r'\((.*?)\)', uuid_salon)
#         uuid_salon = match.group(1)
#         estudiantes = EstudiantesConPromedioYModulos.objects.filter(uuid_salon=uuid_salon)

#         cantidad_estudiantes = estudiantes.count()
#         suma_notas = estudiantes.aggregate(Sum('nota_promedio'))['nota_promedio__sum']

#         if cantidad_estudiantes and suma_notas:
#             promedio_salon = suma_notas / cantidad_estudiantes
#         else:
#             promedio_salon = 0

#         return promedio_salon


class EstatusThinkificSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusThinkific
        fields = '__all__'


class EstatusValuSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusValu
        fields = '__all__'


class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'


class ContenidosColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidosColegio
        fields = '__all__'


class ModuloContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloContenido
        fields = '__all__'


class QuizTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTabla
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class MonitoreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoreo
        fields = '__all__'


class JerarquiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jerarquium
        fields = '__all__'


# class SalonInfoProfeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SalonInfoProfe
#         fields = '__all__'


class EstProfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstProfe
        fields = '__all__'


class EstatusGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusGeneral
        fields = '__all__'


# class SalonKpiModuloSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SalonKpiModulo
#         fields = '__all__'

# class EstudiantesRankingPorModulosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EstudiantesRankingPorModulos
#         fields = [
#             'uuid_mont',
#             'nota_total',
#             'ranking'
#         ]


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Las contraseñas no coinciden.")
#         return data

#     def create(self, validated_data):
#         # Generar un valor de username aleatorio
#         username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

#         user = User.objects.create(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             username=username,  # Asigna el valor de username generado aleatoriamente
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


# # Serializer Test
# class ModuloSerializer(serializers.ModelSerializer):
#     modulo = serializers.CharField()

#     class Meta:
#         model = Estatus
#         fields = [
#             'modulo',
#             'per_completation',
#             'per_videos',
#             'estatus',
#             'nota_quiz1',
#             'nota_quiz2',
#             'nota_quiz3',
#             'nota_quizes',
#             'nota_progreso',
#             'nota_total',
#         ]

class LoginSerializer(serializers.Serializer):
    user_token = serializers.CharField(max_length=255)
