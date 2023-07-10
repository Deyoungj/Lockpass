
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer
from .tokens import get_tokens_for_user


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            
            response = {
                "message": "Registration successfull",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
        # email = request.data.get('email')
        # password = request.data.get('password')

            email = serializer.data['email']
            password = serializer.data['password']
            print("email: ",email)
            print("password: ",password)

        user = authenticate(email=email, password=password)
        

        if user is not None:


            tokens = get_tokens_for_user(user=user)

            response = {
                "message":"login successfull",
                "tokens": tokens
            }

            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message":"invalid email or password"})