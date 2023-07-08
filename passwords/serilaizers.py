from rest_framework import serializers
from .models import Passwords



class PasswordsSerializers(serializers.ModelSerializer):


    class Meta:
        model = Passwords
        fields = ['id', '']