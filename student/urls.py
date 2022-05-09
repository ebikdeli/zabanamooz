from django.urls import path

from . import views


app_name = 'student'

urlpatterns = [
    path('', views.lesson_view, name='lesson_view'),
]
