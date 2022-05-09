from rest_framework import serializers

from student.models import LessonFiles


class LessonFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonFiles
        fields = '__all__'
