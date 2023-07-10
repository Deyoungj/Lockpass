from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import Passwords
from .serilaizers import PasswordsSerializers




@api_view(http_method_names=['GET','POST'])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def passwords(request):
    user = request.user


    if request.method == "POST":
        pass
    passwords = Passwords.objects.filter(user=user)
    serializer = PasswordsSerializers(instance=passwords, many=True)
    

    return Response(data=serializer.data, status=status.HTTP_200_OK)




# class PasswordsView(APIView):
#     serialer_class = PasswordsSerializers

    

# class Passwords(generics.GenericAPIView):

#     pass