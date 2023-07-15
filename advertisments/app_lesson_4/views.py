from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    def homework(request):
        return HttpResponse ( 'Домашка ' )
