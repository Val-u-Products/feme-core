from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if 'non_field_errors' in response.data:
            response.data = {
                'error': 'Inicio de sesión fallido. Por favor, verifica tus credenciales.'
            }

    return response