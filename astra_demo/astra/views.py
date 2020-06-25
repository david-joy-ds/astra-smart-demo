from django.shortcuts import render
from django.http import HttpResponse
from astra.astraPoint.astra_main import connect
from astra.twitApp.twitApp import twitapp
import json

url = "https://cca4ebb0-d9f1-4214-b5ac-53a5532f3b8d-us-east1.apps.astra.datastax.com/api/rest/v1"
post = [connect.connection(url)]

def home(request):
    try:
        s = request.GET.get('q')
        payload = twitapp.tweet(s)
        final_payload = payload
        print(payload)
        insert = connect.insert(url, final_payload)
        print(insert)
        return render(request, 'astra/home.html')
    except:
        return render(request, 'astra/home.html')

def search(request):
    try:
        c = request.GET.get('c')
        data = connect.read(url,c)
        print(data)
        context = {
            'tweets': data
        }
        return render(request, 'astra/search.html', context)
    except:
        return render(request, 'astra/search.html')
def about(request):
    return HttpResponse("About Page")