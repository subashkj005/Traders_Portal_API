from django.conf import settings

from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError
from firebase_admin._auth_utils import InvalidIdTokenError, UserNotFoundError


def firebase_validation(id_token):
    """
    This function receives id token sent by Firebase and
    validate the id token then check if the user exist on
    Firebase or not if exist it returns True else False
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        name = decoded_token.get('name', None)
        try:
            user = auth.get_user(uid)
            if user:
                return {
                    "uid": uid,
                    "email": user.email,
                    "name": name,
                    "registration_method": 'google',
                }
            else:
                return False
        except UserNotFoundError:
            print("Firebase: User not found")
            return False
        except InvalidIdTokenError:
            print(
                'Firebase: Invalid token or unable to decrypt code with current credentials.')
    except ExpiredIdTokenError:
        print("Firebase: Invalid token")
        return False


def get_firebase_config():
    return {
        'apiKey': settings.FIREBASE_CONFIG_API_KEY,
        'authDomain': settings.FIREBASE_CONFIG_AUTH_DOMAIN,
        'projectId': settings.FIREBASE_CONFIG_PROJECT_ID,
        'storageBucket': settings.FIREBASE_CONFIG_STORAGEBUCKET,
        'messagingSenderId': settings.FIREBASE_CONFIG_MESSAGING_SENDER_ID,
        'appId': settings.FIREBASE_CONFIG_APP_ID
    }
