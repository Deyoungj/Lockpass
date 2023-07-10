from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User





class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length =6, write_only=True)
    

    class Meta:
        model = User
        fields=['username','email', 'password']

    def validate(self, attrs):

        email_exist = User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError("This Email already exists")

        return super().validate(attrs)
    


    def create(self, validated_data):

        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user




class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)