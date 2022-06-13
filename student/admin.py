from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import LessonFiles, Student, FileUpload, Prices


admin.site.register(LessonFiles)

class FileUploadInline(GenericTabularInline):
    model = FileUpload


class PricesInline(GenericTabularInline):
    model = Prices


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        FileUploadInline, PricesInline
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register([FileUpload, Prices])
