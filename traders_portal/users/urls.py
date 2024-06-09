from users import views
from django.urls import path

urlpatterns = [
    path('authenticate/', views.SocialSignupAPIView.as_view(), name='social-signin'),
]