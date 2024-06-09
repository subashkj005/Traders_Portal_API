from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.firebase_service import firebase_validation, get_firebase_config
from utils.token_service import get_user_token
from .serializers import UserSerializer
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
           return Response({'message': "Token not provided"})
        
        validated_data = firebase_validation(google_token)

        if not validated_data:
            return Response({'message': 'Invalid token'})
        
        user = Users.objects.filter(uid=validated_data["uid"]).first()
        if user:
            serializer = UserSerializer(user)
            token = get_user_token(user)
            return Response({'data': serializer.data, 
                             'token': token, 
                             'message': 'Login Successful'}, 
                            status=status.HTTP_200_OK)
        else:
            serializer = UserSerializer(data=validated_data)
            if serializer.is_valid():
                serializer.save()
                token = get_user_token(user)
                return Response({'user': serializer.data,
                                 'token': token, 
                                 'message': 'User Created Successfully'}, 
                                status=status.HTTP_201_CREATED)
                
            else:
                return Response({'errors': serializer.errors})
        
                
   
            
