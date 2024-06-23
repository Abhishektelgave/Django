from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def curr_dateTime(request):
    DateTime=datetime.now()
    html=f"<html><body><h1>Current Date and Time:</h1><p>{ DateTime }</p></body></html>"
    return HttpResponse(html)