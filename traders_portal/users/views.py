from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.firebase_service import firebase_validation, get_firebase_config
from utils.token_service import get_user_token
from .serializers import SocialUserRegisterSerializer, UserRegisterSerializer
from .models import Users


def google_login_page(request):
    firebase_config = get_firebase_config()
    return render(request, 'google_login.html', context={'firebase_config': firebase_config})


class SocialSignupAPIView(APIView):

    permission_classes = []
    """
    Api for creating user from social logins
    """

    def post(self, request):
        google_token = request.data.get('token')

        if not google_token:
            return Response({'message': "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = firebase_validation(google_token)

        if not validated_data:
            return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.filter(uid=validated_data["uid"]).first()
        if user:
            serializer = SocialUserRegisterSerializer(user)
            token = get_user_token(user)
            return Response({'data': serializer.data,
                             'token': token,
                             'message': 'Login Successful'},
                            status=status.HTTP_200_OK)
        else:
            serializer = SocialUserRegisterSerializer(data=validated_data)
            if serializer.is_valid():
                serializer.save()
                token = get_user_token(user)
                return Response({'user': serializer.data,
                                 'token': token,
                                 'message': 'User Created Successfully'},
                                status=status.HTTP_201_CREATED)

            else:
                return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(APIView):
    
    permission_classes = []

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    
    permission_classes = [] 
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            return Response({'error': "Email and Passoword required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': "User is not active"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegisterSerializer(user)
        token = get_user_token(user)
        return Response({'user': serializer.data,
                         'token': token,
                         },
                        status=status.HTTP_201_CREATED)
