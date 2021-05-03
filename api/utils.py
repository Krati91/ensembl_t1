from rest_framework.response import Response
from rest_framework import status


def error_prompt(error):
    return Response(
        {'error': str(error)},
        status=status.HTTP_400_BAD_REQUEST
    )
