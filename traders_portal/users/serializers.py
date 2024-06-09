from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Users
        fields = ['id', 'name', 'uid', 'email', 'password', 'registration_method']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Users(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
        