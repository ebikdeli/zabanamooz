from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'student'

router = routers.DefaultRouter()
router.register('lessonfiles', views.LesssonFilesViewSet, 'lessonfiles')

urlpatterns = [
    path('api', include(router.urls)),
    path('', views.lesson_view, name='lesson_view'),
]
