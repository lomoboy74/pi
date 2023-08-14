from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Advertisements
def index(request):
    advertisments=Advertisements.objects.all()
    context={'advertisments':advertisments}
    return render(request, 'index.html',context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisment_post(request):
    from=
    context={'from':from}
    return render(request, 'advertisement-post.html')