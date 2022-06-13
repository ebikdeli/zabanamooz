from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'student'

router = routers.DefaultRouter()
router.register('lessonfiles', views.LesssonFilesViewSet, 'lessonfiles')
router.register('students', views.StudentViewSet, 'students')
router.register('files', views.FileUploadViewSet, 'files')
router.register('prices', views.PricesViewSet, 'prices')

urlpatterns = [
    path('api/', include(router.urls)),
    path('data/', views.student_file_price, name='data'),
    path('', views.lesson_view, name='lesson_view'),
]
