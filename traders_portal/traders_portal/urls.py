from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import google_login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', google_login_page, name="google_login_page"),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/company/', include('companies.urls')),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)