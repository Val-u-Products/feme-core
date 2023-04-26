import secrets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MonitorTabla


@api_view(['PATCH'])
def actualizar_key(request, pk):
    try:
        monitor = MonitorTabla.objects.get(pk=pk)
    except MonitorTabla.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    nueva_key = secrets.token_urlsafe(16)
    monitor.userToken = nueva_key
    monitor.save()
    
    return Response({'userToken': nueva_key}, status=status.HTTP_200_OK)

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