from rest_framework import serializers

from student.models import LessonFiles, Student, FileUpload, Prices


class LessonFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonFiles
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'

class PricesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prices
        fields = '__all__'
