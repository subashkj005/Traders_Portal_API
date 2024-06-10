from users import views
from django.urls import path

urlpatterns = [
    path('authenticate/', views.SocialSignupAPIView.as_view(), name='social-signin'),
    path('register/', views.UserRegisterAPIView.as_view(), name="register_user"),
    path('login/', views.UserLoginAPIView.as_view(), name="login_user"),
]