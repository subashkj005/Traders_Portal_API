from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def get_user_token(user):
    serializer = TokenObtainPairSerializer()
    refresh = serializer.get_token(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token
