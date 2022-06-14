from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class LessonFiles(models.Model):
    name = models.CharField(max_length=300)
    video = models.FileField()
    text = models.TextField(blank=True, null=True, help_text='Optional')


class FileUpload(models.Model):
    file = models.FileField()
    describe = models.CharField(max_length=100, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class Prices(models.Model):
    price = models.PositiveIntegerField()
    describe = models.TextField(blank=True, null=True)
    day = models.PositiveIntegerField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    files = GenericRelation(FileUpload)
    prices = GenericRelation(Prices)
