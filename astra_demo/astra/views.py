from django.shortcuts import render
from django.http import HttpResponse
from astra.astraPoint.astra_main import connect
import json

url = "https://cca4ebb0-d9f1-4214-b5ac-53a5532f3b8d-us-east1.apps.astra.datastax.com/api/rest/v1"
post = [connect.connection(url)]

def home(request):
    context = {
        'posts' : post
    }
    return render(request, 'astra/home.html', context)

def about(request):
    return HttpResponse("About Page")