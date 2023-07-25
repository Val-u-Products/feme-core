# import random
# import string
# import secrets
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(min_length=5, write_only=True)
#     confirm_password = serializers.CharField(min_length=5, write_only=True)
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Las contraseñas no coinciden.")
#         email = data['email']
#         if get_user_model().objects.filter(email=email).exists():
#             raise serializers.ValidationError("Ya existe una cuenta con este correo electrónico.")
#         data['username'] = self.generate_username()
#         return data
    
#     def generate_username(self):
#         username = secrets.token_urlsafe(16)
#         while get_user_model().objects.filter(username=username).exists():
#             username = secrets.token_urlsafe(16)
#         return username

#     def create(self, validated_data):
#         validated_data.pop('confirm_password', None)
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['username'] = self.generate_username()
#         return super().create(validated_data)

    # def validate_password(self, value):
    #     return make_password(value)