from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import (ColeTabla, 
                     EstudiantesTabla, 
                     Modulos, 
                     QuizTabla, 
                     SalonTabla, 
                     MonitorTabla, 
                     SalonKpiModulo,
                     Estatus)
from .serializers import (ColeTablaSerializer, 
                          EstudiantesTablaSerializer, 
                          ModulosSerializer, 
                          QuizTablaSerializer, 
                          SalonTablaSerializer, 
                          MonitorTablaSerializer, 
                          SalonKpiModuloSerializer,
                          EstatusSerializer)


class ColeTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ColeTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ColeTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'uuid_cole', 
                        'colegio', 
                        'ubicacion', 
                        'zona_horaria', 
                        'sexo_colegio', 
                        'zoho_link'
                        ]
    search_fields = [
                    '^uuid_cole', 
                    '^colegio', 
                    '^ubicacion', 
                    '^zona_horaria', 
                    '^sexo_colegio', 
                    '^zoho_link'
                    ]


class EstudiantesTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EstudiantesTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'id_thinkific', 
                        'uuid_mont', 
                        'uuid_cole', 
                        'uuid_salon', 
                        'colegio', 
                        'grado', 
                        'seccion', 
                        'nombres_estudiantes', 
                        'apellidos_estudiantes', 
                        'email',
                        'whatsapp_estudiante',
                        'nombres_representante',
                        'apellidos_representante',
                        'whatsapp_responsable',
                        'email_representante',
                        'inscrito',
                        ]
    search_fields = [
                    '^id_thinkific', 
                    '^uuid_mont', 
                    '^uuid_cole', 
                    '^uuid_salon', 
                    '^colegio', 
                    '^grado', 
                    '^seccion', 
                    '^nombres_estudiantes', 
                    '^apellidos_estudiantes', 
                    '^email',
                    '^whatsapp_estudiante',
                    '^nombres_representante',
                    '^apellidos_representante',
                    '^whatsapp_responsable',
                    '^email_representante',
                    '^inscrito',
                    ]


class ModulosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modulos.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ModulosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id_mol', 'nombre']
    search_fields = ['^id_mol', '^nombre']


class QuizTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuizTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'id_pregunta',
                        'id_mol', 
                        'quiz', 
                        'seccion', 
                        'titulo_de_seccion', 
                        'numero', 
                        'tipo_de_pregunta', 
                        'pregunta',
                        'respuesta_correcta',
                        'respuesta_incorrecta_1',
                        'respuesta_incorrecta_2',
                        'respuesta_incorrecta_3',
                        'respuesta_incorrecta_4',
                        'explicacion_de_la_respueta_correcta',
                        ]
    search_fields = [
                    '^id_pregunta',
                    '^id_mol', 
                    '^quiz', 
                    '^seccion', 
                    '^titulo_de_seccion', 
                    '^numero', 
                    '^tipo_de_pregunta', 
                    '^pregunta',
                    '^respuesta_correcta',
                    '^respuesta_incorrecta_1',
                    '^respuesta_incorrecta_2',
                    '^respuesta_incorrecta_3',
                    '^respuesta_incorrecta_4',
                    '^explicacion_de_la_respueta_correcta',
                    ]


class SalonTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'uuid_salon', 
                        'id_monitor', 
                        'cierre_definitivo', 
                        'l3_22_23', 
                        'l3_22_23_2', 
                        'l3_22_23_au'
                        ]
    search_fields = [
                    '^uuid_salon', 
                    '^id_monitor', 
                    '^cierre_definitivo', 
                    '^l3_22_23', 
                    '^l3_22_23_2', 
                    '^l3_22_23_au'
                    ]



class MonitorTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MonitorTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MonitorTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'uuid_cole', 
                        'uuid_mont', 
                        'monitor', 
                        'materia_feme', 
                        'field_puntaje', 
                        'whatsapp', 
                        'email_m', 
                        'id_thinki_mon', 
                        'userToken'
                        ]
    search_fields = [
                    '^uuid_cole', 
                    '^uuid_mont', 
                    '^monitor', 
                    '^materia_feme', 
                    '^field_puntaje', 
                    '^whatsapp', 
                    '^email_m', 
                    '^id_thinki_mon', 
                    '^userToken'
                    ]


class SalonKpiModuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonKpiModulo.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonKpiModuloSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'uuid_salon', 
                        'id_mol', 
                        'grado', 
                        'seccion', 
                        'modulos', 
                        'total_estudiantes', 
                        'iniciaron', 'llevan50', 
                        'completaron', 
                        'created_at'
                        ]
    search_fields = [
                    '^uuid_salon', 
                    '^id_mol', 
                    '^grado', 
                    '^seccion', 
                    '^modulos', 
                    '^total_estudiantes', 
                    '^iniciaron', 'llevan50', 
                    '^completaron', 
                    '^created_at'
                    ]


class EstatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estatus.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonKpiModuloSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
                        'id_thinkific', 
                        'modulo', 
                        'email', 
                        'started_at', 
                        'expirated_at', 
                        'completed_at', 
                        'per_completation', 
                        'per_videos', 
                        'estatus', 
                        'created_at', 
                        'last_sign_in', 
                        'nota_quiz1', 
                        'nota_quiz2', 
                        'nota_quiz3', 
                        'fecha_q1', 
                        'fecha_q2', 
                        'fecha_q3', 
                        'nota_quizes', 
                        'nota_progreso', 
                        'nota_total', 
                        'nota_total_l'
                        ]
    search_fields = [
                    '^id_thinkific', 
                    '^modulo', 
                    '^email', 
                    '^started_at', 
                    '^expirated_at', 
                    '^completed_at', 
                    '^per_completation', 
                    '^per_videos', 
                    '^estatus', 
                    '^created_at', 
                    '^last_sign_in', 
                    '^nota_quiz1', 
                    '^nota_quiz2', 
                    '^nota_quiz3', 
                    '^fecha_q1', 
                    '^fecha_q2', 
                    '^fecha_q3', 
                    '^nota_quizes', 
                    '^nota_progreso', 
                    '^nota_total', 
                    '^nota_total_l'
                    ]
