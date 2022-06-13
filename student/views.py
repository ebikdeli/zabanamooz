from email.policy import HTTP
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from .models import LessonFiles, Student, FileUpload, Prices
from .forms import LessonFilesModelForms
from .serializers import LessonFilesSerializer, Student, FileUploadSerializer, PricesSerializer, StudentSerializer


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


@csrf_exempt
def student_file_price(request):
    # print(request.COOKIES)
    if request.method == 'POST':
        files = request.FILES
        data = request.POST
        print('files: ', files)
        print('data: ', data)
        return render(request, 'student/student_file_price.html', context={'files': files, 'data': data})
        return HttpResponse('<h1>POSTED!</h1>')
    else:
        return JsonResponse(data='Only "post" method allowed!', safe=False)


class LesssonFilesViewSet(ModelViewSet):
    serializer_class = LessonFilesSerializer
    queryset = LessonFiles.objects.all()


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class FileUploadViewSet(ModelViewSet):
    serializer_class = FileUploadSerializer
    queryset = FileUpload.objects.all()


class PricesViewSet(ModelViewSet):
    serializer_class = PricesSerializer
    queryset = Prices.objects.all()
