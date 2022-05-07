from django.shortcuts import render, HttpResponse


def index(request):
    """Index page of the whole website"""
    return HttpResponse('<h1>Hello ZabanAmooz!</h1>')
