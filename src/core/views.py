# import secrets
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import MonitorTabla
# from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuarios, SalonInfoProfe, RankingEstudiantes, InfoProfe, ActividadCvProfe, ActividadSemanalEstudiantes, ActividadSiguiente
from .serializers import LoginSerializer, InfoProfeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.db.models import Max, Min
from rest_framework.generics import ListAPIView
from rest_framework.filters import BaseFilterBackend
from django_filters import rest_framework as filters
from django.http import Http404




# class UserRegistration(APIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Inicio de sesión exitoso'})
#         else:
#             return Response({'message': 'Correo electrónico o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     return Response({'message': 'Sesión cerrada'})


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def actualizar_key(request, pk):
#     print(pk)
#     try:
#         monitor = MonitorTabla.objects.get(pk=pk)
#     except MonitorTabla.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     nueva_key = secrets.token_urlsafe(12)
#     monitor.userToken = nueva_key
#     monitor.save()
    
#     return Response({'userToken': nueva_key}, status=status.HTTP_200_OK)

# class ActualizarKeyView(APIView):
#     def patch(self, request, uuid_mont):
#         try:
#             monitor = MonitorTabla.objects.get(uuid_mont=uuid_mont)
#         except MonitorTabla.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         nueva_key = secrets.token_urlsafe(16)
#         monitor.key = nueva_key
#         monitor.save()
        
#         return Response({'key': nueva_key}, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_token = serializer.validated_data['user_token']
            try:
                usuario = Usuarios.objects.get(user_token=user_token)
            except Usuarios.DoesNotExist:
                return Response({"error": "Token de acceso inválido"}, status=status.HTTP_401_UNAUTHORIZED)

            # Aquí puedes realizar cualquier otra lógica de autenticación adicional si es necesario

            # Puedes devolver información adicional del usuario si lo deseas
            response_data = {
                "message": "Inicio de sesión exitoso",
                "usuario_nombres": usuario.nombres,
                "usuario_apellidos": usuario.apellidos,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SalonInfoProfeAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Obtener el valor del parámetro id_profe del query params
        id_profe = request.query_params.get('id_profe')

        # Obtener los registros de SalonInfoProfe para el id_profe dado
        queryset = SalonInfoProfe.objects.filter(id_profe=id_profe)

        # Validar si existen registros para el id_profe dado
        if not queryset.exists():
            return Response(status=404, data={'error': 'SalonInfoProfe not found'})

        # Obtener el primer objeto de SalonInfoProfe para obtener el colegio
        primer_registro = queryset.first()
        colegio_data = {
            'uuid_cole': primer_registro.uuid_cole,
            'nombre': primer_registro.colegio
        }

        # Crear la lista de diccionarios para los grados
        grados_data = []
        for registro in queryset:
            grado_data = {
                'uuid_salon': registro.uuid_salon,
                'grado': registro.grado,
                'seccion': registro.seccion,
                'per_completado': f'{registro.per_completados}%',
                'per_pendiente': f'{registro.per_pendiente}%',
                'per_avanzado': f'{registro.per_avanzado}%',
                'per_no_iniciado': f'{registro.per_no_iniciaron}%',
                'per_solo_iniciado': f'{registro.per_solo_iniciado}%',
                'completados': registro.completados,
                'avanzado': registro.avanzado,
                'solo_iniciado': registro.solo_iniciado,
                'no_iniciaron': registro.no_iniciaron,
                'pendiente': registro.pendiente,
                'total_estudiantes': registro.total_estudiantes,
            }
            grados_data.append(grado_data)

        # Crear el JSON final
        response_data = {
            'colegio': colegio_data,
            'grados': grados_data
        }

        return Response(response_data)
    

class TopStudentsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtenemos el valor de 'uuid_salon' del parámetro de consulta
        uuid_salon = request.query_params.get('uuid_salon')

        # Filtramos los estudiantes por 'uuid_salon' si se proporciona
        queryset = RankingEstudiantes.objects.all()
        if uuid_salon:
            queryset = queryset.filter(uuid_salon=uuid_salon)

        # Obtenemos los mejores 5 estudiantes ordenados por 'ranking' de forma ascendente
        top_students = queryset.order_by('ranking')[:5]

        # Obtenemos los peores 5 estudiantes ordenados por 'ranking' de forma descendente
        worst_students = queryset.order_by('-ranking')[:5]

        # Serializamos los datos y los creamos en el formato deseado
        top_students_data = [
            {
                "id_v": student.id_v,
                "nombres": student.nombres,
                "apellidos": student.apellidos,
                "nota_promedio": str(student.nota_promedio),
                "modulos_completados": str(student.modulos_completados),
                "ranking": str(student.ranking),
            }
            for student in top_students
        ]

        worst_students_data = [
            {
                "id_v": student.id_v,
                "nombres": student.nombres,
                "apellidos": student.apellidos,
                "nota_promedio": str(student.nota_promedio),
                "modulos_completados": str(student.modulos_completados),
                "ranking": str(student.ranking),
            }
            for student in worst_students
        ]

        # Creamos el diccionario final con los resultados
        response_data = {
            "top_best_5_students": top_students_data,
            "top_worst_5_students": worst_students_data,
        }

        return Response(response_data)


class IdProfeFilter(filters.FilterSet):
    id_profe = filters.NumberFilter(field_name="id_profe")

    class Meta:
        model = InfoProfe
        fields = ["id_profe"]


class InfoProfeView(ListAPIView):
    serializer_class = InfoProfeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = IdProfeFilter

    def get_queryset(self):
        queryset = InfoProfe.objects.all().distinct('id_profe')
        return queryset
    

static_data_primera = [
    {
        "id_profe" : 3000003,
        "grados": 
        [
            {
                "uuid_salon": "4db75127-2eca-49ae-9df7-9d38a7b044b7",
                "grado": "1er año",
                "seccion": "A",
                "per_completado": "52%",
            },
            {
                "uuid_salon": "1cc8c31d-cb4f-4d2a-9861-4f2194e3adc0",
                "grado": "2do año",
                "seccion": "A",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "1dba069b-a779-4000-a0c3-750017d323ba",
                "grado": "3er año",
                "seccion": "A",
                "per_completado": "69%",
            }
        ]
    },
    {
        "id_profe" : 3000008,
        "grados": 
        [
            {
                "uuid_salon": "7558864d-484c-4adf-8a98-22abb2414af0",
                "grado": "2do año",
                "seccion": "A",
                "per_completado": "59%",
            },
            {
                "uuid_salon": "58bb439d-2ff6-4ce0-b92d-dd3901857cd5",
                "grado": "3er año",
                "seccion": "A",
                "per_completado": "57%",
            }
        ]
    },
    {
        "id_profe" : 3000015,
        "grados": 
        [
            {
                "uuid_salon": "741debe8-b961-4109-9113-019ec8789957",
                "grado": "3er año",
                "seccion": "A",
                "per_completado": "52%",
            },
            {
                "uuid_salon": "02d0ba97-66a2-4e21-ad87-1e6e54c064fe",
                "grado": "3er año",
                "seccion": "B",
                "per_completado": "65%",
            },
            {
                "uuid_salon": "377e1d24-c5a8-45ed-908e-7bffd0c627cc",
                "grado": "3er año",
                "seccion": "C",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "f064ab59-7d60-420a-acfd-8264e12bec5e",
                "grado": "3er año",
                "seccion": "N",
                "per_completado": "91%",
            },
            {
                "uuid_salon": "08db0ab3-63a6-446a-9c52-e21af8641134",
                "grado": "4to año",
                "seccion": "A",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "e8746dba-406a-409a-ab1e-76889a9178cc",
                "grado": "4to año",
                "seccion": "D",
                "per_completado": "22%",
            },
            {
                "uuid_salon": "7d93149c-3d6d-4db0-80bf-03d3985f473e",
                "grado": "4to año",
                "seccion": "N",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "7f10002d-b5ef-443a-b59c-17c28086baa3",
                "grado": "5to año",
                "seccion": "A",
                "per_completado": "16%",
            },
            {
                "uuid_salon": "0ddd2e48-7951-4680-bbb7-b134a3104fe5",
                "grado": "5to año",
                "seccion": "N",
                "per_completado": "72%",
            }
        ]
    },
    {
        "id_profe" : 3000016,
        "grados": 
        [
            {
                "uuid_salon": "57eed45f-46d2-46ee-bc23-a51e4e9530af",
                "grado": "1er año",
                "seccion": "A",
                "per_completado": "95%",
            },
            {
                "uuid_salon": "bbccc264-aec8-4684-b3c5-5ebf382d3a67",
                "grado": "1er año",
                "seccion": "B",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "19fe7f23-f550-4b8d-ad85-4012591e5818",
                "grado": "4to año",
                "seccion": "A",
                "per_completado": "49%",
            },
            {
                "uuid_salon": "2fbb26a6-98a9-46ff-8b0d-dc349a5e7e77",
                "grado": "4to año",
                "seccion": "B",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "c038ec17-1f83-498d-b174-138a9d8018f8",
                "grado": "5to año",
                "seccion": "A",
                "per_completado": "21%",
            },
            {
                "uuid_salon": "9a142bb6-6330-4ff5-8a45-ac2754a0fa65",
                "grado": "5to año",
                "seccion": "B",
                "per_completado": "15%",
            },
            {
                "uuid_salon": "50ece3fc-e768-459d-9e91-f1e76a3c8459",
                "grado": "1er año",
                "seccion": "N",
                "per_completado": "32%",
            },
            {
                "uuid_salon": "80ff5186-bd99-4266-8692-bf33f9493711",
                "grado": "2do año",
                "seccion": "N",
                "per_completado": "45%",
            },
            {
                "uuid_salon": "10826305-aa44-453f-9635-ce9848e2ed6a",
                "grado": "5to año",
                "seccion": "N",
                "per_completado": "53%",
            }
        ]
    }
]


class ProgresoView(APIView):
    def get(self, request, *args, **kwargs):
        id_profe = request.query_params.get('id_profe')

        if id_profe:
            filtered_data = [item for item in static_data_primera if item['id_profe'] == int(id_profe)]
            return Response(filtered_data)
        else:
            return Response(static_data_primera)
        

static_data_segunda = [
    {
        "id_profe": 3000003,
        "salones": 
        [
            {
                "uuid_salon": "4db75127-2eca-49ae-9df7-9d38a7b044b7",
                "nombre_salon": "1er Año A",
                "total_estudiantes": "8",
                "per_completados": "5",
                "per_no_iniciado": "3",
                "title": "Tipos de criptomonedas",
                "description": "Texto",
                "start_date": "18/09/2023"
            },
            {
                "uuid_salon": "1cc8c31d-cb4f-4d2a-9861-4f2194e3adc0",
                "nombre_salon": "2do Año A",
                "total_estudiantes": "4",
                "per_completados": "1",
                "per_no_iniciado": "3",
                "title": "Relaciones",
                "description": "Texto",
                "start_date": "19/09/2023"
            },
            {
                "uuid_salon": "1dba069b-a779-4000-a0c3-750017d323ba",
                "nombre_salon": "3er Año A",
                "total_estudiantes": "4",
                "per_completados": "2",
                "per_no_iniciado": "2",
                "title": "Mercado Municipal: Parte I",
                "description": "Texto",
                "start_date": "20/09/2023"
            }
        ]
    },
    {
        "id_profe": 3000008,
        "salones": 
        [
            {
                "uuid_salon": "7558864d-484c-4adf-8a98-22abb2414af0",
                "nombre_salon": "2do Año A",
                "total_estudiantes": "18",
                "per_completados": "13",
                "per_no_iniciado": "5",
                "title": "Corredores de Bolsa",
                "description": "Texto",
                "start_date": "21/09/2023"
            },
            {
                "uuid_salon": "4db75127-2eca-49ae-9df7-9d38a7b044b7",
                "nombre_salon": "3er Año A",
                "total_estudiantes": "10",
                "per_completados": "8",
                "per_no_iniciado": "2",
                "title": "Online vs Presencial",
                "description": "Texto",
                "start_date": "22/09/2023"
            }
        ]
    },
    {
        "id_profe": 3000015,
        "salones": 
        [
            {
                "uuid_salon": "741debe8-b961-4109-9113-019ec8789957",
                "nombre_salon": "3er Año A",
                "total_estudiantes": "25",
                "per_completados": "17",
                "per_no_iniciado": "8",
                "title": "Nodos",
                "description": "Texto",
                "start_date": "23/09/2023"
            },
            {
                "uuid_salon": "02d0ba97-66a2-4e21-ad87-1e6e54c064fe",
                "nombre_salon": "3er Año B",
                "total_estudiantes": "15",
                "per_completados": "5",
                "per_no_iniciado": "10",
                "title": "Recuento total de transacciones",
                "description": "Texto",
                "start_date": "24/09/2023"
            },
            {
                "uuid_salon": "377e1d24-c5a8-45ed-908e-7bffd0c627cc",
                "nombre_salon": "3er Año C",
                "total_estudiantes": "18",
                "per_completados": "10",
                "per_no_iniciado": "8",
                "title": "Emprendimiento y Finanzas",
                "description": "Texto",
                "start_date": "25/09/2023"
            },
            {
                "uuid_salon": "f064ab59-7d60-420a-acfd-8264e12bec5e",
                "nombre_salon": "3er Año N",
                "total_estudiantes": "31",
                "per_completados": "20",
                "per_no_iniciado": "11",
                "title": "¡Ten Cuidado!",
                "description": "Texto",
                "start_date": "26/09/2023"
            },
            {
                "uuid_salon": "f064ab59-7d60-420a-acfd-8264e12bec5e",
                "nombre_salon": "4to Año A",
                "total_estudiantes": "49",
                "per_completados": "30",
                "per_no_iniciado": "19",
                "title": "Matriculas Universitarias",
                "description": "Texto",
                "start_date": "27/09/2023"
            },
            {
                "uuid_salon": "08db0ab3-63a6-446a-9c52-e21af8641134",
                "nombre_salon": "4to Año A",
                "total_estudiantes": "49",
                "per_completados": "30",
                "per_no_iniciado": "19",
                "title": "Mineros",
                "description": "Texto",
                "start_date": "28/09/2023"
            },
            {
                "uuid_salon": "e8746dba-406a-409a-ab1e-76889a9178cc",
                "nombre_salon": "4to Año D",
                "total_estudiantes": "1",
                "per_completados": "1",
                "per_no_iniciado": "0",
                "title": "Más allá de Wall Street",
                "description": "Texto",
                "start_date": "29/09/2023"
            },
            {
                "uuid_salon": "7d93149c-3d6d-4db0-80bf-03d3985f473e",
                "nombre_salon": "4to Año N",
                "total_estudiantes": "27",
                "per_completados": "19",
                "per_no_iniciado": "8",
                "title": "Halving",
                "description": "Texto",
                "start_date": "20/09/2023"
            },
            {
                "uuid_salon": "7f10002d-b5ef-443a-b59c-17c28086baa3",
                "nombre_salon": "5to Año A",
                "total_estudiantes": "28",
                "per_completados": "9",
                "per_no_iniciado": "19",
                "title": "Microeconomía', 'Actividades clave",
                "description": "Texto",
                "start_date": "21/09/2023"
            },
            {
                "uuid_salon": "0ddd2e48-7951-4680-bbb7-b134a3104fe5",
                "nombre_salon": "5to Año N",
                "total_estudiantes": "41",
                "per_completados": "30",
                "per_no_iniciado": "11",
                "title": "¡Las mejores universidades de Latinoamérica!",
                "description": "Texto",
                "start_date": "22/09/2023"
            }
        ]
    },
    {
        "id_profe": 3000016,
        "salones": 
        [
            {
                "uuid_salon": "57eed45f-46d2-46ee-bc23-a51e4e9530af",
                "nombre_salon": "1er Año A",
                "total_estudiantes": "22",
                "per_completados": "12",
                "per_no_iniciado": "10",
                "title": "Networking: una red laboral",
                "description": "Texto",
                "start_date": "23/09/2023"
            },
            {
                "uuid_salon": "bbccc264-aec8-4684-b3c5-5ebf382d3a67",
                "nombre_salon": "1er Año B",
                "total_estudiantes": "55",
                "per_completados": "39",
                "per_no_iniciado": "16",
                "title": "Instrumentos Financieros - Criptomonedas",
                "description": "Texto",
                "start_date": "24/09/2023"
            },
            {
                "uuid_salon": "50ece3fc-e768-459d-9e91-f1e76a3c8459",
                "nombre_salon": "1er Año N",
                "total_estudiantes": "7",
                "per_completados": "1",
                "per_no_iniciado": "6",
                "title": "Hash Rate & Dificultad",
                "description": "Texto",
                "start_date": "25/09/2023"
            },
            {
                "uuid_salon": "19fe7f23-f550-4b8d-ad85-4012591e5818",
                "nombre_salon": "4to Año A",
                "total_estudiantes": "26",
                "per_completados": "20",
                "per_no_iniciado": "6",
                "title": "Recursos clave",
                "description": "Texto",
                "start_date": "26/09/2023"
            },
            {
                "uuid_salon": "2fbb26a6-98a9-46ff-8b0d-dc349a5e7e77",
                "nombre_salon": "4to Año B",
                "total_estudiantes": "19",
                "per_completados": "11",
                "per_no_iniciado": "8",
                "title": "¡Los protagonistas del sistema bancario!",
                "description": "Texto",
                "start_date": "27/09/2023"
            },
            {
                "uuid_salon": "c038ec17-1f83-498d-b174-138a9d8018f8",
                "nombre_salon": "5to Año A",
                "total_estudiantes": "25",
                "per_completados": "9",
                "per_no_iniciado": "16",
                "title": "Sectores del mercado",
                "description": "Texto",
                "start_date": "28/09/2023"
            },
            {
                "uuid_salon": "9a142bb6-6330-4ff5-8a45-ac2754a0fa65",
                "nombre_salon": "5to Año B",
                "total_estudiantes": "22",
                "per_completados": "21",
                "per_no_iniciado": "1",
                "title": "Tipos de criptomonedas",
                "description": "Texto",
                "start_date": "29/09/2023"
            },
            {
                "uuid_salon": "10826305-aa44-453f-9635-ce9848e2ed6a",
                "nombre_salon": "5to Año N",
                "total_estudiantes": "46",
                "per_completados": "23",
                "per_no_iniciado": "23",
                "title": "estandar",
                "description": "Texto",
                "start_date": "11/09/2023"
            },
            {
                "uuid_salon": "7f10002d-b5ef-443a-b59c-17c28086baa3",
                "nombre_salon": "5to Año A",
                "total_estudiantes": "28",
                "per_completados": "9",
                "per_no_iniciado": "19",
                "title": "Mercado Municipal: Parte I",
                "description": "Texto",
                "start_date": "12/09/2023"
            },
            {
                "uuid_salon": "0ddd2e48-7951-4680-bbb7-b134a3104fe5",
                "nombre_salon": "5to Año N",
                "total_estudiantes": "41",
                "per_completados": "30",
                "per_no_iniciado": "11",
                "title": "Corredores de Bolsa",
                "description": "Texto",
                "start_date": "13/09/2023"
            }
        ]
    }
]


class ProgresoDataView(APIView):
    def get_object_by_id_profe(self, id_profe):
        try:
            return next(item for item in static_data_segunda if item['id_profe'] == id_profe)
        except StopIteration:
            raise Http404

    def get_object_by_uuid_salon(self, uuid_salon):
        try:
            for item in static_data_segunda:
                for salon in item['salones']:
                    if salon['uuid_salon'] == uuid_salon:
                        return {
                            'id_profe': item['id_profe'],
                            'salones': [salon],
                        }
            raise StopIteration
        except StopIteration:
            raise Http404

    def get(self, request, *args, **kwargs):
        id_profe = request.query_params.get('id_profe')
        uuid_salon = request.query_params.get('uuid_salon')

        if id_profe:
            data = self.get_object_by_id_profe(int(id_profe))
            return Response(data)
        elif uuid_salon:
            data = self.get_object_by_uuid_salon(uuid_salon)
            return Response(data)
        else:
            return Response(static_data_segunda)


class CustomJSONView(APIView):
    def get(self, request, uuid_salon):
        data = {
            "uuid_salon": uuid_salon,
            "id_profe": "",
            "grado": "",
            "seccion": "",
            "actividades": [],
        }

        actividad_siguiente = get_object_or_404(ActividadSiguiente, uuid_salon=uuid_salon)
        data["id_profe"] = actividad_siguiente.id_profe
        data["grado"] = actividad_siguiente.grado
        data["seccion"] = actividad_siguiente.seccion
        data["actividades"].append({
            "actividad_siguiente": [{
                "contenido": actividad_siguiente.contenido,
                "titulo": actividad_siguiente.titulo,
                "fecha_siguiente_semana": actividad_siguiente.fecha_siguiente_semana
            }],
            "actividad_semanal_estudiantes": [],
            "actividad_cv_profe": [],
        })

        actividad_semanal_estudiantes = ActividadSemanalEstudiantes.objects.filter(uuid_salon=uuid_salon)
        for actividad in actividad_semanal_estudiantes:
            data["actividades"][0]["actividad_semanal_estudiantes"].append({
                "numero_estudiantes": actividad.numero_estudiantes,
                "lecciones_completadas": actividad.lecciones_completadas,
                "porcentaje_lecciones_completadas": actividad.porcentaje_lecciones_completadas
            })

        actividad_cv_profe = ActividadCvProfe.objects.filter(uuid_salon=uuid_salon)
        for actividad in actividad_cv_profe:
            data["actividades"][0]["actividad_cv_profe"].append({
                "fecha_recom": actividad.fecha_recom,
                "id_mol": actividad.id_mol,
                "pais": actividad.pais,
                "colegio": actividad.colegio,
                "cv": actividad.cv,
                "id_cont": actividad.id_cont,
                "titulo": actividad.titulo,
                "leccion": actividad.leccion,
                "conceptos_clave": actividad.conceptos_claves,
                "objetivos": actividad.objetivos,
                "tiempo": actividad.tiempo,
                "preparacion": actividad.preparacion,
                "materiales": actividad.materiales,
                "resumen": actividad.resumen,
                "descripcion": actividad.descripcion,
                "imagen_descriptiva": actividad.imagen_descriptiva,
                "tipo_actividad": actividad.tipo_actividad,
                "modalidad": actividad.modalidad
            })

        return Response(data)
