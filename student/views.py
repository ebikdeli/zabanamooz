from email.policy import HTTP
from pydoc import describe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from .models import LessonFiles, Student, FileUpload, Prices
from .forms import LessonFilesModelForms
from .serializers import LessonFilesSerializer, Student, FileUploadSerializer, PricesSerializer, StudentSerializer

import re


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
def student_file_price_create(request):
    price_created = 0
    files_uploaded = 0
    # print(request.COOKIES)
    if request.method == 'POST':
        files = dict(request.FILES)
        data = dict(request.POST)
        # print('files: ', files)
        # print('data: ', data)
        
        # return JsonResponse(data=data, safe='False')
        
        # Create or get student by 'name'
        student = None
        name = data.pop('name', None)
        age = data.pop('age', ['0'])
        if not name:
            return JsonResponse(data={'status': 'no', 'message': 'There is no name sent!'}, safe=False)
        student_qs = Student.objects.filter(name=name[0])
        if student_qs.exists():
            student = student_qs.first()
        else:
            student = Student.objects.create(name=name[0], age=int(age[0]))



        # regex patterns for received data
        price_regex = r'price.*'
        price_describe_regex = r'price_describe.*'
        file_describe_regex = r'file_describe.*'
        day_regex = r'day.*'

        # Don't put 'file_describe' (if there is any) in the 'data' dict. Instead put them into 'file_describe_dict'
        file_describe_dict = {k: v for k, v in data.items() if re.search(file_describe_regex, k)}
        # Delete all 'key-values' from 'data' that are common in 'data' and 'file_describe_dict'
        for k in file_describe_dict:
            del data[k]
        # This maybe seems overworking but shows good practise
        file_describe_list = [v[0] for v in file_describe_dict.values()]

        # Process POST data and seprate every data that not part of the 'file' or 'price' process
        # We are doing this by separate every 'key' in 'data' dict if the key does not ends with a digit:
        price_data = {k: v for k, v in data.items() if re.search(r'\d+$', k)}
        #  Delete all 'key-values' from 'data' that are common in 'data' and 'price_data'
        for k in price_data:
            del data[k]

        # If there are any prices data in data, put them into 'student' and db - this one is a little bit tricky!
        # There are many ways we can do this but optimization is very important to us
        if price_data:
            # Using list and sorted to convert 'data' dict to a list sorted by alphabet:
            price_data_list = [(k, v[0]) for k, v in price_data.items()]
            # Sorted 'data_list' be like this: [('day1', '3'), ('day2', '2'), ('price1', '1200000'),
            # ('price2', '20000'), ('price_describe1', ''), ('price_describe2', 'some price')]
            price_data_list = sorted(price_data_list)

            # Because 'Price' model has 3 variables:
            prices_number = len(price_data_list) // 3
            for i in range(prices_number):
                day = int(price_data_list[i][1])
                price = int(price_data_list[i + prices_number][1])
                describe = price_data_list[i + prices_number * 2][1]
                # print('day: ', day, '   describe:   ', describe, '   price: ', price)
                student.prices.create(price=price, describe=describe, day=day)
                price_created += 1
        # print(student.prices.all())

        # If there are files, put them into 'student' and db
        if files:
            i = 0
            for k, v in files.items():
                # print(k, '   ', v)
                student.files.create(file=v[0], describe=file_describe_list[i])
                i += 1
                files_uploaded += 1
        # print(student.files.all())

        # return render(request, 'student/student_file_price.html', context={'files': files, 'data': data})
        # return HttpResponse('<h1>POSTED!</h1>')
        return JsonResponse(data={'status': 'ok', 'file_uploaded': files_uploaded, 'prices_created': price_created}, safe=False)
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
