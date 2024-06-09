from rest_framework_simplejwt.tokens import RefreshToken


def get_user_token(user):
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token
