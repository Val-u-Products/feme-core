from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response
from collections import defaultdict
from rest_framework.authentication import TokenAuthentication

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
                     # SalonInfoProfe,
                     EstProfe,
                     EstatusGeneral,
                     SalonKpiModulo,
                     Actividades
                     )
from .serializers import (ColegioTablaSerializer, 
                          SalonTablaSerializer,
                          RolSerializer,
                          UsuariosSerializer,
                          ValuThinkificSerializer,
                          EstatusThinkificSerializer,
                          EstatusValuSerializer,
                          ModulosSerializer,
                          ContenidosColegioSerializer,
                          ModuloContenidoSerializer,
                          QuizTablaSerializer,
                          FeedbackSerializer,
                          MonitoreoSerializer,
                          JerarquiumSerializer,
                          # SalonInfoProfeSerializer,
                          EstProfeSerializer,
                          EstatusGeneralSerializer,
                          SalonKpiModuloSerializer,
                          ActividadesSerializer
                          )


class ColegioTablaViewSet(viewsets.ModelViewSet):
    queryset = ColegioTabla.objects.all()
    authentication_classes = [TokenAuthentication]  # Requiere autenticación con token
    permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [AllowAny]
    serializer_class = ColegioTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'uuid_cole', 
                        'colegio', 
                        'ubicacion', 
                        'zona_horaria', 
                        'sexo_colegio' 
                        ]
    search_fields = [
                    '^uuid_cole', 
                    '^colegio', 
                    '^ubicacion', 
                    '^zona_horaria', 
                    '^sexo_colegio' 
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
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = SalonTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['uuid_salon', 'cierre_definitivo', 'per_puntaje', 'materia_feme']
    search_fields = ['^uuid_salon', '^cierre_definitivo', '^per_puntaje', '^materia_feme']

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


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = RolSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'rol',
                        'nombre',
                        'permisos'
                        ]
    search_fields = [
                    '^rol',
                    '^nombre',
                    '^permisos' 
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


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.filter(deleted=False)
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = UsuariosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch', 'delete']
    filterset_fields = [
                        'id_v', 
                        'uuid_cole', 
                        'uuid_salon', 
                        'rol', 
                        'colegio', 
                        'grado',
                        'seccion',
                        'nombres',
                        'apellidos',
                        'whatsapp',
                        'email',
                        'inscrito'
                        ]
    search_fields = [
                    '^id_v', 
                    '^uuid_cole', 
                    '^uuid_salon', 
                    '^rol', 
                    '^colegio', 
                    '^grado',
                    '^seccion',
                    '^nombres',
                    '^apellidos',
                    '^whatsapp',
                    '^email',
                    '^inscrito'
                    ]
    
    def get_queryset(self):
        queryset = Usuarios.objects.filter(deleted=False)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        salones = instance.get_salones()
        salon_serializer = SalonKpiModuloSerializer(salones, many=True)
        response_data = serializer.data
        response_data['salones'] = salon_serializer.data
        return Response(response_data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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


class ValuThinkificViewSet(viewsets.ModelViewSet):
    queryset = ValuThinkific.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ValuThinkificSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_thinkific', 
                        'id_v' 
                        ]
    search_fields = [
                    '^id_thinkific', 
                    '^id_v'
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


class EstatusThinkificViewSet(viewsets.ModelViewSet):
    queryset = EstatusThinkific.objects.filter(deleted=False)
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = EstatusThinkificSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch', 'delete']
    filterset_fields = [
                        'id_t',
                        'id_thinkific', 
                        'modulo', 
                        'started_at', 
                        'activated_at', 
                        'expirated_at', 
                        'completed_at', 
                        'per_completacion', 
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
                        'nota_total_l',
                        ]
    search_fields = [
                    '^id_thinkific', 
                    '^id_t',
                    '^id_thinkific', 
                    '^modulo', 
                    '^started_at', 
                    '^activated_at', 
                    '^expirated_at', 
                    '^completed_at', 
                    '^per_completacion', 
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
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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


class EstatusValuViewSet(viewsets.ModelViewSet):
    queryset = EstatusValu.objects.filter(deleted=False)
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = EstatusValuSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_ev',
                        'id_v',
                        'modulo', 
                        'started_at', 
                        'activated_at', 
                        'expirated_at', 
                        'completed_at', 
                        'per_completacion', 
                        'per_videos', 
                        'estatus', 
                        'created_at',
                        'last_sign_in',
                        'nota_quiz1',
                        'nota_quiz2',
                        'nota_quiz3',
                        'intento_quiz1',
                        'intento_quiz2',
                        'intento_quiz3',
                        'fecha_q1',
                        'fecha_q2',
                        'fecha_q3',
                        'nota_total',
                        'nota_total_l'
                        ]
    search_fields = [
                    '^id_skm',
                    '^id_ev',
                    '^id_v',
                    '^modulo', 
                    '^started_at', 
                    '^activated_at', 
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
                    '^intento_quiz1',
                    '^intento_quiz2',
                    '^intento_quiz3',
                    '^fecha_q1',
                    '^fecha_q2',
                    '^fecha_q3',
                    '^nota_total',
                    '^nota_total_l'
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


class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ModulosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_mol', 
                        'nombre' 
                        ]
    search_fields = [
                    '^id_mol', 
                    '^nombre' 
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


class ContenidosColegioViewSet(viewsets.ModelViewSet):
    queryset = ContenidosColegio.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ContenidosColegioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['id_c', 'uuid_salon', 'lapso', 'id_mol', 'c_acceso']
    search_fields = ['^id_c', '^uuid_salon', '^lapso', '^id_mol', '^c_acceso']

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
    

class ModuloContenidoViewSet(viewsets.ModelViewSet):
    queryset = ModuloContenido.objects.all()
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ModuloContenidoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = ['id_mol', 'id_cont', 'orden', 'contenido', 'semana_recom', 'tipo']
    search_fields = ['^id_mol', '^id_cont', '^orden', '^contenido', '^semana_recom', '^tipo']

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
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = QuizTablaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_q',
                        'id_cont',
                        'id_pregunta', 
                        'quiz', 
                        'seccion', 
                        'titulo_de_seccion',
                        'pregunta',
                        'respuesta_correcta',
                        'respuesta_incorrecta_1',
                        'respuesta_incorrecta_2',
                        'respuesta_incorrecta_3',
                        'respuesta_incorrecta_4',
                        'explicacion_correcta'
                        ]
    search_fields = [
                    '^id_q',
                    '^id_cont',
                    '^id_pregunta', 
                    '^quiz', 
                    '^seccion', 
                    '^titulo_de_seccion',
                    '^pregunta',
                    '^respuesta_correcta',
                    '^respuesta_incorrecta_1',
                    '^respuesta_incorrecta_2',
                    '^respuesta_incorrecta_3',
                    '^respuesta_incorrecta_4',
                    '^explicacion_correcta'
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
    

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_f',
                        'id_v',
                        'feedback',
                        'errores'
                        ]
    search_fields = [
                    '^id_f',
                    '^id_v',
                    '^feedback',
                    '^errores'
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
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = MonitoreoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_m',
                        'id_v',
                        'tiempo_sesion',
                        'sign_out',
                        'sign_in',
                        'dia'
                        ]
    search_fields = [
                    '^id_m',
                    '^id_v',
                    '^tiempo_sesion',
                    '^sign_out',
                    '^sign_in',
                    '^dia'
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


class JerarquiumViewSet(viewsets.ModelViewSet):
    queryset = Jerarquium.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = JerarquiumSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']
    filterset_fields = [
                        'id_j',
                        'id_estudiante',
                        'id_coordinador',
                        'id_profe',
                        'id_representante'
                        ]
    search_fields = [
                    '^id_j',
                    '^id_estudiante',
                    '^id_coordinador',
                    '^id_profe',
                    '^id_representante'
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
    

class ActividadesViewSet(viewsets.ModelViewSet):
    queryset = Actividades.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = ActividadesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get']
    filterset_fields = [
                        'id_mol',
                        'titulo',
                        'leccion',
                        'conceptos_claves',
                        'objetivo',
                        'lapso_vz',
                        'lapso_mx',
                        'tiempo',
                        'preparacion',
                        'materiales',
                        'resumen',
                        'descripcion',
                        'imagen_descriptiva',
                        'modalidad',
                        'tipo_actividad',
                        'competencias'
                        ]
    search_fields = [
                    '^id_mol',
                    '^titulo',
                    '^leccion',
                    '^conceptos_claves',
                    '^objetivo',
                    '^lapso_vz',
                    '^lapso_mx',
                    '^tiempo',
                    '^preparacion',
                    '^materiales',
                    '^resumen',
                    '^descripcion',
                    '^imagen_descriptiva',
                    '^modalidad',
                    '^tipo_actividad',
                    '^competencias'
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
    

# class SalonInfoProfeViewSet(viewsets.ModelViewSet):
#     queryset = SalonInfoProfe.objects.all()
#     # authentication_classes = [SessionAuthentication]
#     permission_classes = [AllowAny]
#     serializer_class = SalonInfoProfeSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     http_method_names = ['get']
#     filterset_fields = [
#                         'uuid_cole', 
#                         'uuid_salon', 
#                         'colegio', 
#                         'grado', 
#                         'seccion',
#                         'total_estudiantes',
#                         'per_completados',
#                         'per_avanzado',
#                         'per_solo_iniciado',
#                         'per_no_iniciaron',
#                         'per_pendiente',
#                         'completados',
#                         'avanzado',
#                         'solo_iniciado',
#                         'no_iniciaron',
#                         'pendiente',
#                         'id_profe'
#                         ]
#     search_fields = [
#                     '^uuid_cole', 
#                     '^uuid_salon', 
#                     '^colegio', 
#                     '^grado', 
#                     '^seccion',
#                     '^total_estudiantes',
#                     '^per_completados',
#                     '^per_avanzado',
#                     '^per_solo_iniciado',
#                     '^per_no_iniciaron',
#                     '^per_pendiente',
#                     '^completados',
#                     '^avanzado',
#                     '^solo_iniciado',
#                     '^no_iniciaron',
#                     '^pendiente',
#                     '^id_profe'
#                     ]
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         fields = request.query_params.get('fields', None)
        
#         if fields is None:
#             serializer = self.get_serializer(queryset, many=True)
#             return Response(serializer.data)
                
#         fields_list = fields.split(',')

#         filter_field = None
#         filter_value = None
#         for field in self.filterset_fields:
#             value = request.query_params.get(field)
#             if value is not None:
#                 filter_field = field
#                 filter_value = value
#                 break

#         if filter_field is not None and filter_value is not None:
#             queryset = queryset.filter(**{filter_field: filter_value})

#         response_list = []
#         for item in queryset:
#             item_dict = {}
#             for field in fields_list:
#                 if hasattr(item, field):
#                     item_dict[field] = getattr(item, field)
#             response_list.append(item_dict)

#         return Response(response_list)


class EstProfeViewSet(viewsets.ModelViewSet):
    queryset = EstProfe.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = EstProfeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get']
    filterset_fields = [
                        'id_v',
                        'colegio',
                        'grado',
                        'seccion',
                        'nombres',
                        'apellidos',
                        'whatsapp',
                        'email',
                        'inscrito',
                        'rol',
                        'uuid_cole',
                        'uuid_salon',
                        'user_token',
                        'id_profe',
                        'nombre_monitor',
                        'apellido_monitor'
                        ]
    search_fields = [
                    '^id_v',
                    '^colegio',
                    '^grado',
                    '^seccion',
                    '^nombres',
                    '^apellidos',
                    '^whatsapp',
                    '^email',
                    '^inscrito',
                    '^rol',
                    '^uuid_cole',
                    '^uuid_salon',
                    '^user_token',
                    '^id_profe',
                    '^nombre_monitor',
                    '^apellido_monitor'
                    ]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        salon_estudiantes = defaultdict(list)
        total_estudiantes = 0
        
        for item in queryset:
            salon_key = item.uuid_salon
            grado_key = item.grado
            seccion_key = item.seccion
            estudiante_info = {
                "nombres": item.nombres,
                "apellidos": item.apellidos,
                "id_v": item.id_v,
            }
            salon_estudiantes[salon_key].append((grado_key, seccion_key, estudiante_info))
            total_estudiantes += 1  # Incrementar el contador de estudiantes
        
        response_list = []
        for salon_key, estudiantes_info in salon_estudiantes.items():
            estudiantes = []
            for grado_key, seccion_key, estudiante_info in estudiantes_info:
                estudiantes.append(estudiante_info)
            
            salon_info = {
                "nombre": f"{grado_key} {seccion_key}",
                "uuid_salon": salon_key,
                "estudiantes": estudiantes,
            }
            response_list.append(salon_info)

        # Agregar el campo 'total_estudiantes' a la respuesta
        response_data = {
            "total_estudiantes": total_estudiantes,
            "salones": response_list
        }
        
        return Response(response_data)
    

class EstatusGeneralViewSet(viewsets.ModelViewSet):
    queryset = EstatusGeneral.objects.all()
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = EstatusGeneralSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = ['get']
    filterset_fields = [
                        'id_v',
                        'colegio',
                        'grado',
                        'seccion',
                        'nombres',
                        'apellidos',
                        'modulo',
                        'started_at',
                        'activated_at',
                        'expirated_at',
                        'completed_at',
                        'per_completacion',
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
                        'nota_total',
                        'nota_total_l',
                        'e_acceso',
                        'uuid_salon',
                        'uuid_cole'
                        ]
    search_fields = [
                    '^id_v',
                    '^colegio',
                    '^grado',
                    '^seccion',
                    '^nombres',
                    '^apellidos',
                    '^modulo',
                    '^started_at',
                    '^activated_at',
                    '^expirated_at',
                    '^completed_at',
                    '^per_completacion',
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
                    '^nota_total',
                    '^nota_total_l',
                    '^e_acceso',
                    '^uuid_salon',
                    '^uuid_cole'
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
    http_method_names = ['get']
    filterset_fields = [
                        'total_estudiantes',
                        'estudiantes_iniciados',
                        'estudiantes_50',
                        'estudiantes_completados',
                        'uuid_salon',
                        'grado',
                        'seccion',
                        'modulo',
                        'nombre_monitor',
                        'apellido_monitor'
                        ]
    search_fields = [
                    '^total_estudiantes',
                    '^estudiantes_iniciados',
                    '^estudiantes_50',
                    '^estudiantes_completados',
                    '^uuid_salon',
                    '^grado',
                    '^seccion',
                    '^modulo',
                    '^nombre_monitor',
                    '^apellido_monitor'
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
    