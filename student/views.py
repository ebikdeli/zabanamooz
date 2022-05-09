from django.http import HttpResponse
from django.shortcuts import render

from .models import LessonFiles
from .forms import LessonFilesModelForms


def lesson_view(request):
    if request.method == 'POST':
        lessonfiles_form = LessonFilesModelForms(data=request.POST, files=request.FILES)
        # print(lessonfiles_form)
        if lessonfiles_form.is_valid():
            lessonfiles_form.save()
            return HttpResponse('<h1>Video uploaded successfull</h1>')
        return HttpResponse('<h2>Video did not uploaded!</h2>')
    
    else:
        lessonfiles_form = LessonFilesModelForms()
    lessonfiles = LessonFiles.objects.all()
    
    return render(request, 'student/lesson_view.html', context={'lessonfiles': lessonfiles, 'lessonfiles_form': lessonfiles_form})
