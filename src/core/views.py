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
from .models import Usuarios, SalonInfoProfe, RankingEstudiantes
from .serializers import LoginSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

from django.db.models import Max, Min





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
