from django import forms

from .models import LessonFiles


class LessonFilesModelForms(forms.ModelForm):

    class Meta:
        model = LessonFiles
        fields = '__all__'
