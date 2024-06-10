from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import Users


class SocialUserRegisterSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Users
        fields = ['name', 'uid', 'email', 'password', 'registration_method']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Users(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    

class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Users
        fields = ['name', 'email', 'password', 'confirm_password']

    def validate_email(self, value):
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = Users.objects.create_user(**validated_data)
        return user
        