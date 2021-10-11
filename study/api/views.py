from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#기본 페이지
def index(request):
    return HttpResponse("index page 다")