from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import Passwords


@api_view(http_method_names=['GET','POST'])
def passwords(request):
    
    data = Passwords.objects.all()

    return Response(data=data, status=status.HTTP_200_OK)
