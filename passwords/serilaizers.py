from rest_framework import serializers
from .models import Passwords



class PasswordsSerializers(serializers.ModelSerializer):
    # passwords = serializers.StringRelatedField(many=True)
    class Meta:
        model = Passwords
        fields = ['id', 'site_name', 'site_password', 'date_added', 'user']
        # read_only_fields = ("user",)