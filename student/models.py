from django.db import models


class LessonFiles(models.Model):
    name = models.CharField(max_length=300)
    video = models.FileField()
    text = models.TextField(blank=True, null=True, help_text='Optional')
