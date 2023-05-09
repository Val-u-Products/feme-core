from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
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
                     Estatus)
from .serializers import (ColeTablaSerializer, 
                          EstudiantesTablaSerializer, 
                          ModulosSerializer, 
                          QuizTablaSerializer, 
                          SalonTablaSerializer, 
                          MonitorTablaSerializer, 
                          SalonKpiModuloSerializer,
                          EstatusSerializer)


class ColeTablaViewSet(viewsets.ModelViewSet):
    queryset = ColeTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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


class EstudiantesTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstudiantesTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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


class ModulosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modulos.objects.all()
    authentication_classes = [JWTAuthentication]
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


class QuizTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuizTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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


class SalonTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonTabla.objects.all()
    authentication_classes = [JWTAuthentication]
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



class MonitorTablaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MonitorTabla.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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


class SalonKpiModuloViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalonKpiModulo.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalonKpiModuloSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
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


class EstatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estatus.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
