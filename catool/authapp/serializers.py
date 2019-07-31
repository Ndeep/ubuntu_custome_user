from rest_framework import serializers
from authapp.models import User

from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=125)
    password2=serializers.CharField(max_length=125)
    class Meta:
        model=User
        field=('email','first_name','account','staff','admin','active')

    def validate_confirm_password(self):
        password1 = self.validated_data.get("password1")
        password2 = self.validated_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Passwords don't match")
        return password2
