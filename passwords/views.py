from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import Passwords
from .serilaizers import PasswordsSerializers

# testing alll views


@api_view(http_method_names=['GET','POST'])
@permission_classes(permission_classes=[permissions.IsAuthenticated])
def passwords(request):
    user = request.user


    if request.method == "POST":
        data = request.data

        serializer = PasswordsSerializers(data=data)

        if serializer.is_valid():
            serializer.save(user=user)

            responseData = {
                'data': serializer.data
            }
            return Response(data=responseData, status=status.HTTP_200_OK)
        



    # passwords = Passwords.objects.filter(user=user)
    passwords = Passwords.objects.all()
    serializer = PasswordsSerializers(instance=passwords, many=True)
    

    return Response(data=serializer.data, status=status.HTTP_200_OK)



    
@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def view_or_update_or_delete_password(request, pk):

    user = request.user

    if request.method == "GET":
        
        password = Passwords.objects.filter(pk=pk)

        serialzer = PasswordsSerializers(instance=password, many=True)

        return Response(data=serialzer.data, status=status.HTTP_200_OK)




# class PasswordsView(APIView):
#     serialer_class = PasswordsSerializers

    

# class Passwords(generics.GenericAPIView):

#     pass

