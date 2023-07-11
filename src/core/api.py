from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

from .models import (ColeTabla, 
                     EstudiantesTabla, 
                     Modulos, 
                     QuizTabla, 
                     SalonTabla, 
                     MonitorTabla, 
                     SalonKpiModulo,
                     Estatus,
                     Monitoreo,
                     Feedback,
                     EstudiantesConPromedioYModulos,
                     EstudiantesRankingPorModulos
                     )
from .serializers import (ColeTablaSerializer, 
                          EstudiantesTablaSerializer, 
                          ModulosSerializer, 
                          QuizTablaSerializer, 
                          SalonTablaSerializer, 
                          MonitorTablaSerializer, 
                          SalonKpiModuloSerializer,
                          EstatusSerializer,
                          MonitoreoSerializer,
                          FeedbackSerializer,
                          EstudiantesConPromedioYModulosSerializer,
                          EstudiantesRankingPorModulosSerializer
                          )


class ColeTablaViewSet(viewsets.ModelViewSet):
    queryset = ColeTabla.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ColeTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ModulosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['id_mol', 'nombre']
    search_fields = ['^id_mol', '^nombre']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class QuizTablaViewSet(viewsets.ModelViewSet):
    queryset = QuizTabla.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuizTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_q',
                        'id_pregunta',
                        'id_mol', 
                        'quiz', 
                        'seccion', 
                        'titulo_de_seccion', 
                        'pregunta',
                        'respuesta_correcta',
                        'respuesta_incorrecta_1',
                        'respuesta_incorrecta_2',
                        'respuesta_incorrecta_3',
                        'respuesta_incorrecta_4',
                        'explicacion_de_la_respueta_correcta',
                        ]
    search_fields = [
                    '^id_q',
                    '^id_pregunta',
                    '^id_mol', 
                    '^quiz', 
                    '^seccion', 
                    '^titulo_de_seccion', 
                    '^pregunta',
                    '^respuesta_correcta',
                    '^respuesta_incorrecta_1',
                    '^respuesta_incorrecta_2',
                    '^respuesta_incorrecta_3',
                    '^respuesta_incorrecta_4',
                    '^explicacion_de_la_respueta_correcta',
                    ]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class SalonTablaViewSet(viewsets.ModelViewSet):
    queryset = SalonTabla.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class MonitorTablaViewSet(viewsets.ModelViewSet):
    queryset = MonitorTabla.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = MonitorTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class EstudiantesTablaViewSet(viewsets.ModelViewSet):
    queryset = EstudiantesTabla.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = EstudiantesTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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
                        'whatsapp_representante',
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
                    '^whatsapp_representante',
                    '^email_representante',
                    '^inscrito',
                    ]
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class SalonKpiModuloViewSet(viewsets.ModelViewSet):
    queryset = SalonKpiModulo.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = SalonKpiModuloSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_skm',
                        'uuid_salon',
                        'id_mol', 
                        'grado', 
                        'seccion', 
                        'modulo', 
                        'total_estudiantes', 
                        'iniciaron', 
                        'llevan50', 
                        'completaron', 
                        'created_at'
                        ]
    search_fields = [
                    '^id_skm',
                    '^uuid_salon',
                    '^id_mol', 
                    '^grado', 
                    '^seccion', 
                    '^modulo', 
                    '^total_estudiantes', 
                    '^iniciaron', 
                    '^llevan50', 
                    '^completaron', 
                    '^created_at'
                    ]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        orden = request.GET.get('orden', 'descendente')
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class EstatusViewSet(viewsets.ModelViewSet):
    queryset = Estatus.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = EstatusSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)


class MonitoreoViewSet(viewsets.ModelViewSet):
    queryset = Monitoreo.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MonitoreoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['id_m', 'id_thinki_mon', 'tiempo_sesion', 'sign_in', 'sign_out','dia']
    search_fields = ['^id_m', '^id_thinki_mon', '^tiempo_sesion', '^sign_in', '^sign_out','^dia']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)
    

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['id_f', 'id_thinki_mon', 'feedback', 'errores', 'fecha']
    search_fields = ['^id_f', '^id_thinki_mon', '^feedback', '^errores', '^fecha']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)
    

class EstudiantesConPromedioYModulosViewSet(viewsets.ModelViewSet):
    queryset = EstudiantesConPromedioYModulos.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = EstudiantesConPromedioYModulosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'nombres_estudiantes',
                        'apellidos_estudiantes',
                        'uuid_salon', 
                        'id_thinkific', 
                        'nota_promedio', 
                        'modulos_completados',
                        'ranking'
                        ]
    search_fields = [
                    '^nombres_estudiantes',
                    '^apellidos_estudiantes',
                    '^uuid_salon', 
                    '^id_thinkific', 
                    '^nota_promedio', 
                    '^modulos_completados',
                    '^ranking'
                    ]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)
    

class EstudiantesRankingPorModulosViewSet(viewsets.ModelViewSet):
    queryset = EstudiantesRankingPorModulos.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = EstudiantesRankingPorModulosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'nombres_estudiantes',
                        'apellidos_estudiantes',
                        'uuid_salon',
                        'modulo',
                        'id_thinkific', 
                        'nota_total', 
                        'id_modulo',
                        'ranking'
                        ]
    search_fields = [
                    '^nombres_estudiantes',
                    '^apellidos_estudiantes',
                    '^uuid_salon',
                    '^modulo',
                    '^id_thinkific', 
                    '^nota_total', 
                    '^id_modulo',
                    '^ranking'
                    ]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = request.query_params.get('fields', None)
        
        if fields is None:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
                
        fields_list = fields.split(',')

        filter_field = None
        filter_value = None
        for field in self.filterset_fields:
            value = request.query_params.get(field)
            if value is not None:
                filter_field = field
                filter_value = value
                break

        if filter_field is not None and filter_value is not None:
            queryset = queryset.filter(**{filter_field: filter_value})

        response_list = []
        for item in queryset:
            item_dict = {}
            for field in fields_list:
                if hasattr(item, field):
                    item_dict[field] = getattr(item, field)
            response_list.append(item_dict)

        return Response(response_list)
    