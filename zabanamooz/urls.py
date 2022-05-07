"""
https://docs.djangoproject.com/en/4.0/topics/http/urls/#passing-extra-options-to-view-functions
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# This is for 'Token based authentication in rest-framework:
# from rest_framework.authtoken import views as token_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vitrin.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('token-auth/', token_view.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
