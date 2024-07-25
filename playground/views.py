from django.shortcuts import render
from django.http import HttpResponse

def dummy(request):
    return HttpResponse('Hello')
# Create your views here.

